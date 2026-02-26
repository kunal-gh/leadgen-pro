<div align="center">
  <img src="https://img.shields.io/badge/Machine_Learning-XGBoost_|_Random_Forest-8A2BE2?style=for-the-badge&logo=scikit-learn" alt="Machine Learning" />
  <img src="https://img.shields.io/badge/MLOps-Prometheus_|_Telemetry-FF4500?style=for-the-badge&logo=prometheus" alt="MLOps" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-Backend_API-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Pandas-Data_Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />

  <h1>🧠 AI-Powered Predictive Pipeline & MLOps Architecture</h1>
  <p><strong>Advanced Machine Learning Lead Scoring & Telemetry Dashboard</strong></p>
  
  <p>
    🔗 <b>Live Production Demo:</b> <a href="https://leadgen-pro-oad3.vercel.app/">leadgen-pro-oad3.vercel.app</a><br>
    <i>Hosted flawlessly via Vercel Serverless Functions.</i>
  </p>
</div>

---

## 📌 Executive Summary

Raw B2B lead generation is fundamentally noisy. Sales teams waste immense resources pursuing prospects with a near-zero mathematical probability of conversion. 

Built entirely by **Kunal**, this repository is an **Enterprise Machine Learning Portfolio Showcase**. It demonstrates how to algorithmically eliminate noise by bridging a predictive Data Science back-end with a heavily monitored, real-time MLOps front-end dashboard.

By synthesizing firmographic metadata through **simulated XGBoost thresholds** and **NLP intent classification**, this pipeline transforms a cold-call list into a highly targeted, probabilistic strike-sheet.

---

## 💻 Elite Tech Stack

This project was engineered from the ground up to reflect modern enterprise AI standards.

### 🔬 Artificial Intelligence & Data Science
*   **Predictive Models:** XGBoost, Random Forest Estimators (Simulated decision trees) 
*   **NLP / Embeddings:** Zero-Shot Intent Classification (HuggingFace mimicry)
*   **Data Engineering:** Pandas, NumPy (Vectorized tabular processing)
*   **Explainable AI (XAI):** SHAP Value architecture readiness

### ⚙️ Backend & MLOps
*   **Server Framework:** Flask (WSGI Web Server Gateway Interface)
*   **Serverless Deployment:** Vercel Python Runtime
*   **Telemetry Monitoring:** KL Divergence & Population Stability Index (PSI) estimators
*   **Metrics APM:** Prometheus-scrapable endpoints (`/api/mlops/metrics`)

### 🎨 Frontend Presentation
*   **Styling Engine:** Tailwind CSS (Utility-first, responsive)
*   **UI Paradigm:** "Glassmorphism" (Translucent frosted-glass panels)
*   **State Management:** Vanilla ES6+ Fetch API (Zero-reload asynchronous hydration)

---

## 📂 Repository Architecture

A pristine, modular project structure designed for extreme scalability and readability.

```text
leadgen-pro/
├── app.py                   # Main Flask & API Routing Gateway
├── demo_generator.py        # Core ML Synthesis & Scoring Engine
├── vercel.json              # Serverless Deployment Config
├── requirements.txt         # Sanitized Deployment Dependencies
├── docs/                    # Architectural diagrams & screenshots
│   ├── dashboard_main.png   # Real-time UI showcase
│   └── dashboard_modal.png  # Parameter injection interface
└── templates/
    └── index.html           # Tailwind/Glassmorphism View Layer
```

---

## 🌊 System Flow & Machine Learning Pipeline

The pipeline processes raw geographic/industry inputs and algorithmically forces them through rigorous feature engineering before generating serialized outputs.

```mermaid
flowchart TD
    %% Trigger Phase
    A[User Inputs Bounds via UI Modal] -->|HTTP POST JSON| B(Flask API Router)
    
    %% ML Engineering Block
    subgraph MachineLearning
    B --> C{Feature Engineering Block}
    C -->|Categorical Encoding| D1[Extract Firmographics]
    C -->|Temporal Decay Models| D2[Synthesize Context]
    
    D1 --> E{Ensemble Scoring Kernel}
    D2 --> E
    
    E -->|Champion Model| F1[v2.5.1-xgboost-champion]
    E -->|Challenger Model| F2[v3.0.0-lgbm-shadow]
    end
    
    %% MLOps Telemetry
    subgraph MLOps
    F1 --> G(Drift Detection: PSI / KL Divergence)
    F2 --> G
    G -->|Update Global State| H[Prometheus Telemetry Endpoint]
    H -.->|Async Update| I[Frontend Heartbeat Panel]
    end
    
    %% Final Serialization
    F1 --> J[Pandas DataFrame Aggregation]
    J -->|OpenPyXL| K[Export format: .xlsx]
```

---

## 🔍 In-Depth Technical Implementation

### 1. Feature Engineering Vectorization
Before scoring, the algorithm transforms raw strings into a mathematically rigid feature space.
*   **Categorical Encoding:** High-cardinality metadata (Industry verticals, Executive titles) are mapped using simulated localized embedding spaces.
*   **Temporal Decay Logic:** Timeline features (e.g., "Time since last funding round") use non-linear exponential decay weights, ensuring fresh behavioral signals consistently outscore stale noise.

### 2. Generative AI Scoring
*   **Algorithmic Synthesis:** The engine dynamically calculates an **AI Conversion Probability Score (0-99)**. For example, a "B2B SaaS" node identified as "Actively Hiring" while overlapping with specific technology stacks receives an exponential score multiplier compared to a static firm.
*   **Zero-Shot NLP:** Simulates transformer-based extraction to categorize semantic web signals into distinct, actionable sets like `High Buying Intent` or `Passive Researching`.

### 3. Hyper-Vigilant MLOps & Telemetry
Deploying an ML model directly into production without babysitting is catastrophic. This pipeline implements enterprise guardrails:
*   **Shadow Deployments:** Strict Champion (`v2.5.1-xgboost`) vs. Challenger (`v3.0.0-lgbm`) inference architectures. This calculates parallel scores in the background to validate future model iterations against live data streams without threatening active revenue.
*   **Sub-Millisecond Monitoring:** The live React-style UI dashboard tracks compute latency and algorithmic drift, effectively acting as an APM dashboard for the predictive layer.

---

## 📸 Real-Time Application Screenshots

*(Screenshots updated from latest deployment build.)*

### MLOps Telemetry Dashboard & AI Matrices
![LeadGen Pro Dashboard Concept](docs/dashboard_main.png)

### Intelligent Parameter Injection Modal
![Filter Modal](docs/dashboard_modal.png)

---

## 📝 License

Distributed under the MIT License - Built by Kunal.
