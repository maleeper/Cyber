"""Generate a ydata-profiling report for the cybersecurity intrusion dataset."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import pandas as pd
from ydata_profiling import ProfileReport


def build_profile(dataset_path: Path, output_path: Path) -> Path:
    """Create a ydata-profiling report for ``dataset_path`` and save it to ``output_path``."""
    df = pd.read_csv(dataset_path)

    profile = ProfileReport(
        df,
        title="Cybersecurity Intrusion Dataset Profile",
        explorative=True,
        progress_bar=True,
        dataset={
            "description": (
                "Automated exploratory analysis generated with ydata-profiling for the "
                "cybersecurity intrusion dataset."
            )
        },
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    profile.to_file(output_path)
    return output_path


def main() -> None:
    dataset_path = REPO_ROOT / "data" / "raw" / "cybersecurity_intrusion_data.csv"
    output_path = REPO_ROOT / "reports" / "cybersecurity_intrusion_profile.html"

    report_path = build_profile(dataset_path, output_path)
    print(f"Profiling report saved to: {report_path}")


if __name__ == "__main__":
    main()
