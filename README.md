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

## Tableau Dashboard
The Tableau Public version of the dashboard is available [here](https://public.tableau.com/views/Cyber_Hack3/CyberStory?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link). 

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
- [Tableau Dashboard](https://public.tableau.com/views/Cyber_Hack3/CyberStory?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

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

- **streamlit / dash** — dashboard development

---

## Credits
**Content:**
- Dataset: [Cybersecurity Intrusion Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/dnkumars/cybersecurity-intrusion-detection-dataset)
- Tutorials and methods inspired by scikit-learn, SHAP documentation.
- Generative AI such as ChatGPT and Copilot are used for ideation, code snippets and optimisation.
- Machine learning notebooks adapted from Code Institute course materials.

**Media:**
- Icons: [Font Awesome](https://fontawesome.com/)
- Diagrams: Open-source graphics under CC0

---

| **Feature Name**          | **Category**              | **Description** |
|-----------------------------|----------------------------|-----------------|
| `network_packet_size`       | Network-Based             | Represents the size of network packets (64–1500 bytes). Small packets (~64 bytes) may be control messages; large packets (~1500 bytes) carry bulk data. Abnormally small or large packets can indicate reconnaissance or exploitation. |
| `protocol_type`             | Network-Based             | Communication protocol used in the session: **TCP** (reliable, common for HTTP/HTTPS/SSH), **UDP** (fast, less reliable, used in VoIP/streaming), or **ICMP** (network diagnostics, often abused in DoS attacks). |
| `encryption_used`           | Network-Based             | Encryption protocol: **AES** (strong), **DES** (weak, outdated), or **None** (unencrypted). Attackers might avoid encryption or use weak ones to exploit vulnerabilities. |
| `login_attempts`            | User Behavior-Based       | Number of login attempts. Typical users: 1–3. High values may indicate brute-force attacks with hundreds or thousands of attempts. |
| `session_duration`          | User Behavior-Based       | Session length in seconds. Very long sessions may indicate unauthorized access or an attacker maintaining persistence. |
| `failed_logins`             | User Behavior-Based       | Number of failed login attempts. High values suggest credential stuffing or dictionary attacks. A pattern of many failed attempts followed by a success could indicate compromise. |
| `unusual_time_access`       | User Behavior-Based       | Binary flag (0 or 1) indicating login at an unusual time. Attackers often access systems outside normal business hours to evade detection. |
| `ip_reputation_score`       | User Behavior-Based       | A score (0–1) representing IP trustworthiness. Higher scores indicate more suspicious activity (e.g., botnets, spam, or prior attacks). |
| `browser_type`              | User Behavior-Based       | User’s browser (Chrome, Firefox, Edge, Safari, etc.). Unknown browsers could indicate bots or automated scripts. |
| `attack_detected`           | **Target Variable**       | Binary classification target: **1** = attack detected, **0** = normal activity. |

---
#  Glossary

| Term | Definition |
|------|-------------|
| **AI (Artificial Intelligence)** | The simulation of human intelligence by machines to perform tasks such as learning, reasoning, and decision-making. Used here for intrusion detection and pattern recognition. |
| **Anomaly Detection** | Identifying unusual patterns in network traffic that may indicate malicious activity. |
| **Benign** | This means harmless, not malicious, or legitimate.|
| **Confusion Matrix** | A table summarizing true/false positives and negatives, used to evaluate model performance. |
| **Data Imputation** | Filling in missing data with estimated or computed values to maintain dataset integrity. |
| **Dashboard Responsiveness** | How quickly and smoothly a data visualization interface reacts to user input or filtering. |
| **EDA (Exploratory Data Analysis)** | The process of summarizing and visualizing data to discover structure, trends, and anomalies. |
| **ETL (Extract, Transform, Load)** | A standard data pipeline process: extracting data, transforming it for analysis, and loading it into storage. |
| **Feature Engineering** | Creating or modifying input features to improve model accuracy or interpretability. |
| **Feature Importance** | Quantitative measure of how much each variable contributes to the model’s predictions. |
| **False Positive** | A benign event incorrectly classified as an attack, leading to false alerts. |
| **K-Fold Cross-Validation** | A model evaluation method where data is split into *k* parts to train and test multiple times for robustness. |
| **Machine Learning (ML)** | Algorithms that learn patterns from data to make predictions or classifications. |
| **Model Explainability** | The ability to understand and communicate how a model arrives at its predictions. |
| **Normalization** | Scaling numeric data to a consistent range to improve comparability and model stability. |
| **Precision** | The ratio of true positives to all predicted positives, representing accuracy of detected intrusions. |
| **ROC-AUC (Receiver Operating Characteristic - Area Under Curve)** | A performance measure for classification models indicating how well they distinguish between classes. |
| **SHAP (SHapley Additive exPlanations)** | A method to interpret ML model outputs by showing the contribution of each feature to individual predictions. |
| **Stratified Sampling** | Sampling method that preserves the distribution of target classes in the training data. |
| **Streamlit / Tableau / Power BI** | Tools for creating interactive dashboards and data visualizations. |
| **Cyber Threat Intelligence (CTI)** | Knowledge about potential or active cyber threats that supports detection and defense strategies. |
| **Model Calibration** | Adjusting a model so predicted probabilities better match observed outcomes. |
| **Explainable AI (XAI)** | Techniques that make complex AI systems interpretable and transparent to users. |
| **UDP** | User Datagram Protocol. It's a fast, connectionless internet protocol that sends data packets without a prior handshake or guaranteed delivery.|
| **TP** | This is a true positive meaning the predictions accurately determined it was an attack. |
| **TN** | This is true negative meaning the predictions accurately determined that it wasn't an attack |
| **FP** | This is a false positive meaning the predictions falsley determined it was an attack |
| **FN** | This is true negative meaning the predictions falsley determined that it wasn't an attack, So an attack was missed. |

---

## Acknowledgements
Thanks to Neil and Vasi at **Code Institute** and Hackathon organisers, mentors, and teammates for feedback and collaboration.

---

*End of README — Ready for submission and presentation!*

