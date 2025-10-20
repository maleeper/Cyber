# Project Cyber — Cybersecurity Intrusion Detection

## Streamlit Dashboard Quickstart

The repository now includes a Streamlit application that recreates the Tableau EDA dashboard (`reports/Cyberv4.pdf`).

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch the dashboard

```bash
streamlit run streamlit_app.py
```

The app loads the processed dataset from `data/processed/cybersecurity_intrusion_data_eda.csv`. Use the sidebar to pick the
binary target column (e.g., `attack_detected`), adjust the feature threshold slider, and apply categorical/numeric filters.

### 3. Explore the tabs

- **Overview:** Usage guidance and context for the dataset.
- **Data:** Scrollable table of the processed dataset with a CSV download button.
- **EDA:** Tableau-inspired visuals displaying attack metrics by protocol, encryption, browsing behaviour, and session
  characteristics.

## Downloading the presentation

To share the five-slide stakeholder deck (`reports/Cyber_intrusion_story.pptx`) directly from your machine:

1. From the repository root, start a lightweight local web server:

   ```bash
   python -m http.server 8000
   ```

2. Open your browser to [http://localhost:8000/reports/Cyber_intrusion_story.pptx](http://localhost:8000/reports/Cyber_intrusion_story.pptx) to download the presentation file.

3. Press `Ctrl+C` in the terminal when you are finished sharing the link.

### Rebuilding the deck without committing binaries

If repository policies prevent you from raising pull requests with binary files, you can
recreate the deck from the template in code:

1. Install the slide dependency if it is not already available:

   ```bash
   pip install python-pptx
   ```

2. Run the helper script to generate `reports/Cyber_intrusion_story.pptx` locally:

   ```bash
   python scripts/build_presentation.py
   ```

The script loads `Cyber_pres.pptx`, applies the house styling, and writes the same
five-slide story used for stakeholder reviews. Share the regenerated file however your
workflow requires.

---

**Project Cyber** is a comprehensive data analysis and dashboarding project developed during the **Data Analytics with AI Hackathon: Dashboard Essentials (4 Days)**, organised in collaboration with **Code Institute**. It focuses on cybersecurity intrusion detection — analysing network traffic, identifying malicious patterns, and visualising results through an interactive dashboard using **Python**, **Power BI**, or **Tableau Public**.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

> This README follows the hackathon template and is pre-filled for the **Cybersecurity Intrusion Detection Dataset**. Replace project-specific details as needed to match your final implementation.

---

## Dataset Content
- **Dataset name / link:** [Cybersecurity Intrusion Detection Dataset](https://www.kaggle.com/datasets/dnkumars/cybersecurity-intrusion-detection-dataset)
- **Domain:** Network Security & Intrusion Detection
- **Objective:** Detect malicious traffic patterns in network logs using machine learning.
- **Schema overview:**
  - Features describing network flows (e.g., `protocol`, `src_port`, `dst_port`, `packet_count`, etc.)
  - Target column indicates whether the flow is benign or intrusion.
- **Size & format:** The file cybersecurity_intrusion_data.csv contains **9,537 **records of network activity with a unique session ID (session_id) and 10 features used for intrusion detection. It includes attributes like packet size, protocol type, login attempts, session duration, encryption type, IP reputation score,failed logins, browser type, unusual time access, and a binary attack detection label (attack_detected).

- **License:** Public dataset (verify Kaggle licence before publishing results).

**Preprocessing:** Stratified sampling to maintain class balance and reduce size. Handle missing values, normalise numeric fields, and encode categorical features.

---

## Automated Profiling

Generate an automated exploratory data analysis report for the raw dataset with [ydata-profiling](https://github.com/ydataai/ydata-profiling):

```bash
python scripts/generate_cybersecurity_profile.py
```

The script saves an HTML report to `reports/cybersecurity_intrusion_profile.html`, which can be opened locally in a browser for detailed insights and data quality checks.

---

## Business Requirements
- Build an interactive cybersecurity dashboard for monitoring and detecting intrusion patterns.
- Enable filtering by protocol, IP, and port for in-depth exploration.
- Provide trend and frequency analysis of attack types.
- Display feature importance and model explainability results (SHAP, feature weights).
- Include export and alerting options for flagged anomalies.

**Constraints:** Ensure performance with large datasets, prioritise high precision (minimise false positives), and preserve user privacy (mask IPs).

---

## Hypothesis and Validation
1. **Hypothesis 1:** High packet counts and unusual port usage indicate potential intrusions.
   - *Validate:* Feature importance and SHAP analysis confirm contribution of packet count to classification.

2. **Hypothesis 2:** Intrusions cluster at specific hours or traffic spikes.
   - *Validate:* Time-series and correlation analysis of intrusion events.

3. **Hypothesis 3:** Certain protocols have higher intrusion risk (e.g., ICMP or TCP).
   - *Validate:* Compare intrusion rates across protocols using bar charts and chi-square tests.

**Acceptance Criteria:**
- Precision ≥ 0.90  
- False Positive Rate ≤ 5%  
- Model calibration error within 3% tolerance

---

## Project Plan
| Day | Focus | Deliverables |
|-----|--------|---------------|
| **Day 1** | Ideation & ETL setup | Dataset selection, cleaning, repo setup |
| **Day 2** | EDA & Dashboard Prototyping | Visuals, first model run, hypothesis formulation |
| **Day 3** | Refinement & Documentation | Final visuals, README, presentation draft |
| **Day 4** | Final Presentation | Submit dashboard, presentation, and documentation |

**Workflow:** ETL → EDA → Modelling → Visualisation → Storytelling → Presentation

**Tools:** Python, Pandas, Scikit-learn, Plotly, SHAP, Power BI / Tableau

---

## Mapping Business Requirements to Visualisations
| Business Requirement | Visualisation | Rationale |
|----------------------|----------------|------------|
| Monitor intrusions over time | Line chart with filters | Detect spikes & temporal anomalies |
| Analyse protocols & ports | Treemap / stacked bar | Identify most vulnerable connections |
| Detect unusual flows | Scatter / box plots | Spot outliers and extreme behaviour |
| Explain model decisions | SHAP summary / waterfall | Transparency & trust in AI outputs |
| Drill into suspicious traffic | Interactive table | Investigate anomalies by feature |

---

## Analysis Techniques
- **Data Cleaning:** Imputation, type coercion, duplicate removal
- **Feature Engineering:** One-hot encoding, scaling, log transforms, aggregation
- **EDA:** Histograms, correlation heatmaps, pair plots, class imbalance analysis
- **Modelling:** Logistic Regression, Random Forest, XGBoost
- **Validation:** Stratified K-fold cross-validation, ROC-AUC & Precision-Recall metrics
- **Explainability:** SHAP feature attribution and PDP plots

**Generative AI usage:** Ideation for hypotheses, code optimisation, and README drafting, with manual validation and ethical verification.

---

## Ethical Considerations
- **Data Privacy:** Mask IP addresses and sensitive fields.
- **Fairness:** Validate that model decisions aren’t biased toward specific data segments.
- **Transparency:** Document assumptions, model versions, and false positive rates.
- **Compliance:** Respect dataset licence and ensure no personal or organisational identifiers remain.

---

## Dashboard Design
**Pages:**
1. **Overview:** KPIs, intrusion trends, total alerts.
2. **Protocol Insights:** Attack frequency by protocol and port.
3. **Feature Importance:** Model drivers visualised with SHAP.
4. **Temporal Analysis:** Intrusion frequency by hour/day.
5. **Flow Explorer:** Interactive filtering of specific records.

**Widgets:** Search, dropdown filters (protocol, IP, port), export buttons, and interactive legends.

**Communication:**
- Non-technical: plain English summaries, colour-coded insights.
- Technical: metrics, confusion matrices, feature importance charts.

---

## Unfixed Bugs
- Slow filtering on high-cardinality categorical fields (e.g., IPs).
- Class imbalance in rare intrusion types → unstable thresholds.
- Limited interactivity with very large datasets.

*Mitigations:* Aggregation, caching, and using stratified sampling.

---

## Development Roadmap
- **Challenges:** Handling large data, maintaining explainability, improving dashboard responsiveness.
- **Solutions:** Sampling, incremental learning, pre-computed summaries.
- **Future Learning:** DAX optimisation, Tableau extensions, streaming ML (Kafka), better SHAP visual integration.

---

## Deployment

### Tableau
- [Tableau Dashboard](https://public.tableau.com/views/Cyberv4_17607073035910/CyberStory?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Heroku (if Streamlit/Flask)
1. Log in to Heroku → Create App
2. Connect to GitHub → Select repo → Deploy branch
3. Click **Open App** once deployed
4. Use `.slugignore` to exclude large non-app files



**Example Project Structure:**
```
📁 project-cyber/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── etl_pipeline.ipynb
│   └── analysis.ipynb
│
├── dashboards/
│   ├── cyber_dashboard.pbix
│   └── cyber_tableau.twbx
│
├── src/
│   ├── data_cleaning.py
│   └── analysis_utils.py
│
├── README.md
└── requirements.txt
```

---

## Main Data Analysis Libraries
- **pandas / numpy** — ETL and preprocessing
- **scikit-learn** — modelling & evaluation
- **matplotlib / plotly / seaborn** — visualisation
- **shap / eli5** — explainability
# ![CI logo](https://github.com/Kaznolan/Cyber/blob/main/reports/SHAP1.png?raw=true)

# ![CI logo](https://github.com/Kaznolan/Cyber/blob/main/reports/SHAP2.png?raw=true)

- **streamlit / dash** — dashboard development (if web-based)

---

## Credits
**Content:**
- Dataset: [Cybersecurity Intrusion Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/dnkumars/cybersecurity-intrusion-detection-dataset)
- Tutorials and methods inspired by scikit-learn, SHAP documentation.
- Generative AI such as ChatGPT and Copilot are used for ideation, code snippets and optimisation.

**Media:**
- Icons: [Font Awesome](https://fontawesome.com/)
- Diagrams: Open-source graphics under CC0

---

## Acknowledgements
Thanks to the **Code Institute**, Hackathon organisers, mentors, and teammates for feedback and collaboration.

---

*End of README — Ready for submission and presentation!*

