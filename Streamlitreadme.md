# Project Cyber — Cybersecurity Intrusion Detection

## Streamlit Dashboard Quickstart

The repository now includes a Streamlit application that recreates the Tableau EDA dashboard (`reports/Cyberv4.pdf`).  Which has some errors but we run out of time to troublesheet it.

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

*