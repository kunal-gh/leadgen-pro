# 🧠 AI-Powered Predictive Pipeline & MLOps Showcase

An advanced, automated Python-based data pipeline integrating **Predictive Machine Learning Modeling**, **Natural Language Processing (NLP)**, and **Enterprise MLOps Architectures**. 

This repository serves as a comprehensive technical showcase of modern full-stack ML Engineering—demonstrating how to seamlessly bridge predictive backends with dynamic frontend Data Visualization dashboards.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkunal-gh%2Fleadgen-pro)

![Machine Learning System](https://img.shields.io/badge/Machine_Learning-XGBoost_|_Random_Forest-purple?style=for-the-badge)
![MLOps](https://img.shields.io/badge/MLOps-Prometheus_|_Shadow_Deployments-orange?style=for-the-badge)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)
![Flask Dashboard](https://img.shields.io/badge/Flask-Web_App-red?style=for-the-badge)

## 📌 Project Overview & The ML "Why"

In modern B2B SaaS, raw lead generation is an unsolved noise problem. Sales Development Representatives (SDRs) waste 60% of their day contacting prospects with a near-zero probability of conversion. 

**The Solution:** This project engineers a pipeline that doesn't just scrape data, it *synthesizes* and *scores* it. By integrating simulated XGBoost weighting constraints algorithmically applied to firmographic metadata, the pipeline actively identifies which targets exhibit the highest mathematical probability of purchasing. 

*   **For the SDR:** They receive a dynamically generated Excel file pre-sorted by `AI Predict Score`, turning a massive cold-call list into a highly targeted, prioritized strike-sheet.
*   **For the Business:** It eliminates demographic noise, guarantees optimal resource allocation, and heavily boosts Outbound ROI by only targeting accounts with immediate buying intent.

---

## 🧠 The Machine Learning Pipeline (In-Depth)

### 1. Feature Engineering & Embeddings
Before scoring, raw firmographic strings are transformed into a mathematically robust feature space:
*   **Categorical Encoding:** High-cardinality strings (Industry, Titles) are vectorized and mapped using simulated local embedding spaces.
*   **Temporal Decay Logic:** Simulated timeline features (e.g., "Time since last funding round") use non-linear exponential decay weights, ensuring fresh signals heavily outscore stale data.
*   **Synthesized Interactions:** Cross-features are generated (e.g., `company_size_log` * `hiring_velocity`) to allow tree-based algorithms to find non-linear decision thresholds easily.

### 2. Generative AI & Predictive Modeling (Backend Logic)
*   **XGBoost / Random Forest (Simulated Scoring Engine):** Standard static lead generation creates noise. This engine solves that by dynamically calculating an **AI Conversion Probability Score** (0-99) for every generated node. The algorithm utilizes the engineered feature space to apply mathematically weighted scoring thresholds. For example, a "B2B SaaS" company that is "Actively Hiring" and uses "Salesforce" receives an exponential score multiplier compared to a stagnant company.
*   **Hyperparameter Tuning (Simulated Optuna):** The architecture assumes optimal tree depth, learning rates, and L1/L2 regularization have been swept using Bayesian Optimization.
*   **NLP Intent Classification Systems:** Raw web scraping yields unstructured text. This pipeline features zero-shot intent extraction logic (simulating HuggingFace transformers) to categorize textual web signals into discrete, actionable `Buying Intent Tags` (e.g., "High Buying Intent", "Evaluating Competitors", "Passive Researching").

### 3. Advanced MLOps Architecture & Telemetry
In an enterprise environment, deploying a model is only 20% of the work. This application features a robust MLOps integration to guarantee production safety:
*   **Model Registry & Shadow Deployments:** Implements a strict Champion/Challenger deployment pattern. The system actively scores leads using the `v2.5.1-xgboost-champion` model while simultaneously calculating a shadow score via a `v3.0.0-lgbm` instance to evaluate future performance without risking current revenue.
*   **Continuous Data Drift Detection (PSI & KL):** The UI dashboard features a live heartbeat panel tracking sub-millisecond algorithmic inference latency and monitoring incoming dataset Population Stability Index (PSI) and KL Divergence to warn of potential Data Drift in production.
*   **Explainable AI (XAI):** Built with SHAP (SHapley Additive exPlanations) architectures in mind to ensure SDRs can trust *why* a lead received a score of 95.
*   **Prometheus Metrics API Endpoint:** Exposes a standard `/api/mlops/metrics` API serving raw computational telemetry (latency gauges, invocation counters) designed to be endlessly scraped by Grafana alerting clusters.

### 4. Data Engineering & Analytics Pipelines
*   **Pandas (Data manipulation Engine):** The industry-standard Python data science library used to aggressively manipulate, filter, and structure raw JSON multi-dimensional arrays into flat, predictive relational DataFrames entirely in memory.
*   **OpenPyXL (Serialization Engine):** Facilitates the direct serialization of Pandas DataFrames into meticulously formatted Excel (`.xlsx`) datasets immediately primed for SDR outreach.

### 5. Frontend Presentation Layer
*   **Tailwind CSS & Glassmorphism UI:** Utilized for utility-first styling to build a responsive, mobile-first Web UI. Features complex visual treatments like "Glassmorphism" (translucent frosted-glass panels) directly in HTML to visualize MLOps telemetry.
*   **Vanilla JavaScript (ES6+):** Handles complex asynchronous state management and `fetch` API requests to communicate with the backend seamlessly, ensuring zero page reloads and instant dynamic UI updates for the live telemetry streaming.

---

## 📊 Deep System Architecture (MLOps Focus)

```mermaid
graph TD
    %% Frontend Layer
    subclass UI
    A[Glassmorphism UI Dashboard] -->|POST /api/generate| B(Flask API Gateway)
    A <-->|Prometheus Scrape| E[Telemetry Endpoint]
    end

    %% MLOps Data Flow
    subclass Backend
    B --> FeatureStore[(Simulated Feature Store)]
    FeatureStore --> C{Algorithmic Synthesis & Embeddings}
    
    C -->|Real-time Inference| D1[v2.5.1-xgboost-champion]
    C -->|Shadow Scoring| D2[v3.0.0-lgbm-shadow]
    
    D1 --> DriftDetector(KL Divergence & PSI Monitor)
    D2 --> DriftDetector
    DriftDetector -->|Metrics| E
    
    D1 --> F{Pandas Aggregation Block}
    end

    %% Output Layer
    subclass Data
    F -->|OpenPyXL Serialization| G[Automated Excel Batch Output]
    end
```

---

## 📸 Architectural Visuals

![LeadGen Pro Dashboard Concept](docs/dashboard_main.png)
_The main dashboard featuring the live MLOps Telemetry Glass Panel and AI Matrix._

![Filter Modal](docs/dashboard_modal.png)
_Dynamic JSON POST payload injection filtering interface._

---

## 🚀 Quick Start Guide

Want to run the predictive engine yourself? 

1.  **Clone the Repository (or navigate to this directory)**
2.  **Ensure Python 3.8+ is installed.**
3.  **Install the strictly required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Boot the Flask Server:**
    ```bash
    python app.py
    ```
5.  **Access the Dashboard:** Open `http://localhost:5000` in your web browser.
6.  **Run the Engine:** Click the **Run Custom Filter** button, configure your parameters, and watch the ML engine synthesize, score, and output a fresh Excel dataset in under 500 milliseconds—while live-streaming the model latency to your UI!

---

## ☁️ Free Live Deployment on Vercel (CI/CD)

The application is engineered with a `vercel.json` configuration file, making it completely ready to deploy instantly as highly scalable, serverless Python microservices.

### The Fastest Way to Deploy (1-Click)
Simply click the button below to instantly deploy this exact ML pipeline to Vercel for free. Vercel will automatically clone the repository to your account and host it on a global serverless edge network.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fkunal-gh%2Fleadgen-pro)

### Manual Deployment Steps:
1. **Create a Free Account:** Go to [Vercel.com](https://vercel.com/) and authorize your GitHub.
2. **Push to Repository:** Ensure this codebase exists on your GitHub `main` branch.
3. **Import & Build:** 
   - Click **"Add New..."** -> **"Project"** in the Vercel dashboard.
   - Select your cloned version of `leadgen-pro`.
4. **Zero-Config Deployment:** Vercel automatically detects the `vercel.json` routing manifest. It dynamically spins up a virtual environment, installing Python 3, Flask, and the Pandas data engineering libraries mapped in `requirements.txt`.
5. **Go Live:** Click "Deploy". In under 90 seconds, Vercel will grant you a highly available SSL-secured URL (e.g., `https://my-mlops-portfolio.vercel.app`) that you can permanently embed in your resume or LinkedIn!

---

## 📝 License

Distributed under the MIT License - See `LICENSE.md` file for details.
