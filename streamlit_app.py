"""Streamlit dashboard replicating Cyberv4 Tableau EDA."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Tuple

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path("data/processed/cybersecurity_intrusion_data_eda.csv")


@st.cache_data(show_spinner=False)
def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the processed cybersecurity dataset."""
    df = pd.read_csv(path)
    return df


def get_categorical_columns(df: pd.DataFrame) -> Iterable[str]:
    """Return names of categorical columns."""
    return df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()


def get_numeric_columns(df: pd.DataFrame) -> Iterable[str]:
    """Return names of numeric columns."""
    return df.select_dtypes(include=["number"]).columns.tolist()


def is_binary(series: pd.Series) -> bool:
    """Check whether a series contains exactly two distinct non-null values."""
    return series.dropna().nunique() == 2


def apply_filters(
    df: pd.DataFrame,
    categorical_filters: Dict[str, Iterable[str]],
    numeric_filters: Dict[str, Tuple[float, float]],
) -> pd.DataFrame:
    """Apply categorical and numeric filters to the dataframe."""
    filtered = df.copy()
    for column, values in categorical_filters.items():
        if values:
            filtered = filtered[filtered[column].isin(values)]
    for column, (min_value, max_value) in numeric_filters.items():
        filtered = filtered[(filtered[column] >= min_value) & (filtered[column] <= max_value)]
    return filtered


def prepare_binary_target(series: pd.Series) -> pd.Series:
    """Return a binary (0/1) representation of the target column."""
    if series.dtype == bool:
        return series.astype(int)
    if np.issubdtype(series.dtype, np.number):
        unique_values = sorted(series.dropna().unique())
        if set(unique_values).issubset({0, 1}):
            return series.astype(int)
    mapping = {value: index for index, value in enumerate(sorted(series.dropna().unique()))}
    return series.map(mapping)


def overview_tab_content(df: pd.DataFrame) -> None:
    """Render the overview tab."""
    st.subheader("How to Use This Dashboard")
    st.markdown(
        """
        - **Purpose:** Explore network session characteristics that contribute to cybersecurity intrusions.
        - **Tabs:**
            - **Overview:** Instructions and context for the dataset.
            - **Data:** Inspect the processed dataset used in this analysis.
            - **EDA:** Interact with Tableau-inspired visuals and drill into the data using filters.
        - **Sidebar Controls:**
            - Select the *target column* used to compute attack metrics. The target must be binary (e.g., `attack_detected`).
            - Choose a *threshold feature* and adjust the slider to focus on sessions above a chosen value.
            - Refine the dataset with categorical selections and numeric range sliders.
        - **Insights:** The visuals highlight attack prevalence by protocol, encryption, and browsing behaviour while
          contrasting session duration, IP reputation, and failed logins for suspicious activity.
        """
    )

    st.subheader("Dataset Snapshot")
    st.write(
        "The `cybersecurity_intrusion_data_eda.csv` file contains engineered features for 8,807 sessions, "
        "including packet size, login attempts, encryption type, and whether an attack was detected."
    )
    st.dataframe(df.head(10))


def data_tab_content(df: pd.DataFrame) -> None:
    """Render the data tab."""
    st.subheader("Data Used in the Dashboard")
    st.caption("Below is the processed dataset powering the visual analysis.")
    st.dataframe(df, use_container_width=True, height=480)

    st.download_button(
        label="Download data as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="cybersecurity_intrusion_data_eda.csv",
        mime="text/csv",
    )


def eda_tab_content(
    df: pd.DataFrame,
    filtered_df: pd.DataFrame,
    target_column: str,
    threshold_column: str,
    threshold_value: float,
) -> None:
    """Render the EDA tab with charts."""
    st.subheader("Exploratory Data Analysis")

    if filtered_df.empty:
        st.warning("No records match the current filter selection. Adjust the sidebar filters to continue.")
        return

    if not is_binary(df[target_column]):
        st.error(
            "The selected target column is not binary. Choose a column with exactly two unique values in the sidebar "
            "to display the EDA metrics."
        )
        return

    binary_target = prepare_binary_target(filtered_df[target_column])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sessions (filtered)", f"{len(filtered_df):,}")
    with col2:
        st.metric("Attack Count", int(binary_target.sum()))
    with col3:
        attack_rate = binary_target.mean() * 100 if len(filtered_df) else 0
        st.metric("Attack Rate", f"{attack_rate:.1f}%")

    st.caption(
        f"Threshold applied: `{threshold_column}` ≥ {threshold_value:.3f}. {binary_target.sum()} sessions exceed the threshold."
    )

    charts_container = st.container()

    with charts_container:
        chart_cols = st.columns(2)

        if "protocol_type" in filtered_df.columns:
            protocol_summary = (
                filtered_df.assign(attack=binary_target)
                .groupby("protocol_type")[["attack"]]
                .agg(["mean", "sum", "count"])
            )
            protocol_summary.columns = ["Attack Rate", "Attack Count", "Sessions"]
            protocol_summary = protocol_summary.reset_index()
            fig_protocol = px.bar(
                protocol_summary,
                x="protocol_type",
                y="Attack Count",
                color="Attack Rate",
                color_continuous_scale="Reds",
                text="Sessions",
                title="Attack Count by Protocol Type",
            )
            fig_protocol.update_layout(coloraxis_colorbar=dict(title="Attack Rate"))
            chart_cols[0].plotly_chart(fig_protocol, use_container_width=True)

        if "encryption_used" in filtered_df.columns:
            encryption_summary = (
                filtered_df.assign(attack=binary_target)
                .groupby("encryption_used")[["attack"]]
                .agg(["mean", "sum"])
            )
            encryption_summary.columns = ["Attack Rate", "Attack Count"]
            encryption_summary = encryption_summary.reset_index()
            fig_encryption = px.bar(
                encryption_summary,
                x="encryption_used",
                y="Attack Rate",
                color="Attack Count",
                color_continuous_scale="Blues",
                title="Attack Rate by Encryption Used",
            )
            fig_encryption.update_yaxes(tickformat=".0%")
            chart_cols[1].plotly_chart(fig_encryption, use_container_width=True)

        chart_cols = st.columns(2)

        if {"session_duration", target_column}.issubset(filtered_df.columns):
            fig_duration = px.box(
                filtered_df.assign(attack=binary_target),
                x=target_column,
                y="session_duration",
                color=target_column,
                title="Session Duration by Attack Detection",
            )
            chart_cols[0].plotly_chart(fig_duration, use_container_width=True)

        if {"ip_reputation_score", "fail_ratio"}.issubset(filtered_df.columns):
            fig_scatter = px.scatter(
                filtered_df,
                x="ip_reputation_score",
                y="fail_ratio",
                color=binary_target,
                color_continuous_scale=[[0, "#2c7fb8"], [1, "#d7191c"]],
                title="IP Reputation vs. Failed Login Ratio",
                labels={"color": "Attack"},
                hover_data=["protocol_type", "encryption_used", target_column],
            )
            chart_cols[1].plotly_chart(fig_scatter, use_container_width=True)

        if "unusual_time_access" in filtered_df.columns:
            trend_df = (
                filtered_df.assign(attack=binary_target)
                .groupby("unusual_time_access")[["attack"]]
                .agg(["mean", "sum", "count"])
            )
            trend_df.columns = ["Attack Rate", "Attack Count", "Sessions"]
            trend_df = trend_df.reset_index().sort_values("unusual_time_access")
            fig_trend = px.line(
                trend_df,
                x="unusual_time_access",
                y="Attack Count",
                markers=True,
                title="Attack Count by Unusual Access Window",
            )
            st.plotly_chart(fig_trend, use_container_width=True)

        if {"network_packet_size", "login_attempts", target_column}.issubset(filtered_df.columns):
            heat_df = (
                filtered_df.assign(attack=binary_target)
                .groupby([pd.cut(filtered_df["network_packet_size"], bins=5), pd.cut(filtered_df["login_attempts"], bins=5)])
                .attack.mean()
                .reset_index()
            )
            heat_df.rename(columns={"network_packet_size": "Packet Size Bin", "login_attempts": "Login Attempts Bin", "attack": "Attack Rate"}, inplace=True)
            fig_heatmap = px.density_heatmap(
                heat_df,
                x="Packet Size Bin",
                y="Login Attempts Bin",
                z="Attack Rate",
                color_continuous_scale="OrRd",
                title="Attack Rate by Packet Size and Login Attempts",
            )
            fig_heatmap.update_layout(xaxis_nticks=36, yaxis_nticks=36)
            st.plotly_chart(fig_heatmap, use_container_width=True)


def build_sidebar(df: pd.DataFrame) -> Tuple[str, str, float, pd.DataFrame]:
    """Render sidebar filters and return filtered dataframe along with selections."""
    st.sidebar.header("Configuration")

    target_options = df.columns.tolist()
    default_target = "attack_detected" if "attack_detected" in target_options else target_options[0]
    target_column = st.sidebar.selectbox("Target column", options=target_options, index=target_options.index(default_target))

    if not is_binary(df[target_column]):
        st.sidebar.error("Selected target column is not binary. Metrics will be unavailable until a binary column is chosen.")

    numeric_columns = get_numeric_columns(df)
    default_threshold_column = "fail_ratio" if "fail_ratio" in numeric_columns else numeric_columns[0]
    threshold_column = st.sidebar.selectbox(
        "Feature threshold column",
        options=numeric_columns,
        index=numeric_columns.index(default_threshold_column),
    )

    min_threshold = float(df[threshold_column].min())
    max_threshold = float(df[threshold_column].max())
    default_threshold = float(np.median(df[threshold_column]))

    if max_threshold > min_threshold:
        step_size = max((max_threshold - min_threshold) / 100, 1e-6)
    else:
        step_size = 1.0

    threshold_value = st.sidebar.slider(
        "Threshold value",
        min_value=min_threshold,
        max_value=max_threshold,
        value=default_threshold,
        step=step_size,
    )

    categorical_filters: Dict[str, Iterable[str]] = {}
    numeric_filters: Dict[str, Tuple[float, float]] = {}

    with st.sidebar.expander("Categorical filters", expanded=False):
        for column in get_categorical_columns(df):
            options = sorted(df[column].dropna().unique())
            if not options:
                continue
            default = options
            selected = st.multiselect(column, options=options, default=default)
            if set(selected) != set(options):
                categorical_filters[column] = selected

    with st.sidebar.expander("Numeric ranges", expanded=False):
        for column in numeric_columns:
            col_min = float(df[column].min())
            col_max = float(df[column].max())
            if col_min == col_max:
                continue
            default_range = (col_min, col_max)
            selected_range = st.slider(column, min_value=col_min, max_value=col_max, value=default_range)
            if selected_range != default_range:
                numeric_filters[column] = selected_range

    filtered_df = apply_filters(df, categorical_filters, numeric_filters)
    filtered_df = filtered_df[filtered_df[threshold_column] >= threshold_value]

    return target_column, threshold_column, threshold_value, filtered_df


def main() -> None:
    """Application entry point."""
    st.set_page_config(
        page_title="Cybersecurity Intrusion EDA",
        layout="wide",
        page_icon="🛡️",
    )

    st.title("Cybersecurity Intrusion Analysis Dashboard")
    st.caption("Replicating the insights from the Cyberv4 Tableau exploratory analysis in Streamlit.")

    if not DATA_PATH.exists():
        st.error(
            "Data file not found. Please ensure `data/processed/cybersecurity_intrusion_data_eda.csv` is available "
            "in the repository."
        )
        return

    df = load_data(DATA_PATH)

    target_column, threshold_column, threshold_value, filtered_df = build_sidebar(df)

    tabs = st.tabs(["Overview", "Data", "EDA"])

    with tabs[0]:
        overview_tab_content(df)

    with tabs[1]:
        data_tab_content(df)

    with tabs[2]:
        eda_tab_content(df, filtered_df, target_column, threshold_column, threshold_value)


if __name__ == "__main__":
    main()
