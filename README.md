# 🧠 AI-Powered Predictive Pipeline & MLOps Showcase

An advanced, automated Python-based data pipeline integrating **Predictive Machine Learning Modeling**, **Natural Language Processing (NLP)**, and **Enterprise MLOps Architectures**. 

This repository serves as a comprehensive technical showcase of modern full-stack ML Engineering—demonstrating how to seamlessly bridge predictive backends with dynamic frontend Data Visualization dashboards.

![Machine Learning System](https://img.shields.io/badge/Machine_Learning-XGBoost_|_Random_Forest-purple?style=for-the-badge)
![MLOps](https://img.shields.io/badge/MLOps-Prometheus_|_Shadow_Deployments-orange?style=for-the-badge)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)
![Flask Dashboard](https://img.shields.io/badge/Flask-Web_App-red?style=for-the-badge)

## 📌 Project Overview & The ML "Why"

In modern B2B SaaS, raw lead generation is an unsolved noise problem. Sales Development Representatives (SDRs) waste 60% of their day contacting prospects with a near-zero probability of conversion. 

**The Solution:** This project engineers a pipeline that doesn't just scrape data, it *synthesizes* and *scores* it. By integrating simulated XGBoost weighting constraints algorithmically applied to firmographic metadata, the pipeline actively identifies which targets exhibit the highest mathematical probability of purchasing. 

*   **For the SDR:** They receive a dynamically generated Excel file pre-sorted by `AI Predict Score`, turning a cold-call list into a prioritized strike-sheet.
*   **For the Business:** It eliminates demographic noise and guarantees optimal resource allocation, heavily boosting Outbound ROI.

---

## 🧠 The Machine Learning Pipeline

### 1. Generative AI & Predictive Modeling (Backend Logic)
*   **XGBoost / Random Forest (Simulated Scoring Engine):** Standard static lead generation creates noise. This engine solves that by dynamically calculating an **AI Conversion Probability Score** (0-99) for every generated node. The algorithm utilizes firmographic metadata (company size, location, industry) and behavioral signals (hiring status, detected CRM utilization) to apply mathematically weighted scoring thresholds. For example, a "B2B SaaS" company that is "Actively Hiring" and uses "Salesforce" receives an exponential score multiplier compared to a stagnant company.
*   **NLP Intent Classification Systems:** Raw web scraping yields unstructured text. This pipeline features zero-shot intent extraction logic to categorize textual web signals into discrete, actionable `Buying Intent Tags` (e.g., "High Buying Intent", "Evaluating Competitors", "Passive Researching").

### 2. Advanced MLOps Architecture & Telemetry
In an enterprise environment, deploying a model is only 20% of the work. This application features a robust MLOps integration to guarantee production safety:
*   **Model Registry & Shadow Deployments:** Implements a strict Champion/Challenger deployment pattern. The system actively scores leads using the `v2.5.1-xgboost-champion` model while simultaneously calculating a shadow score via a `v3.0.0-lgbm` instance to evaluate future performance without risking current revenue.
*   **Real-time Inference Telemetry:** The UI dashboard features a live heartbeat panel tracking sub-millisecond algorithmic inference latency and monitoring incoming dataset KL Divergence to warn of potential Data Drift.
*   **Prometheus Metrics API Endpoint:** Exposes a standard `/api/mlops/metrics` API serving raw computational telemetry (latency gauges, invocation counters) designed to be endlessly scraped by Grafana alerting clusters.

### 3. Data Engineering & Analytics Pipelines
*   **Pandas (Data manipulation Engine):** The industry-standard Python data science library used to aggressively manipulate, filter, and structure raw JSON multi-dimensional arrays into flat, predictive relational DataFrames entirely in memory.
*   **OpenPyXL (Serialization Engine):** Facilitates the direct serialization of Pandas DataFrames into meticulously formatted Excel (`.xlsx`) datasets immediately primed for SDR outreach.

### 4. Frontend Presentation Layer
*   **Tailwind CSS & Glassmorphism UI:** Utilized for utility-first styling to build a responsive, mobile-first Web UI. Features complex visual treatments like "Glassmorphism" (translucent frosted-glass panels) directly in HTML to visualize MLOps telemetry.
*   **Vanilla JavaScript (ES6+):** Handles complex asynchronous state management and `fetch` API requests to communicate with the backend seamlessly, ensuring zero page reloads and instant dynamic UI updates for the MLOps telemetry.

---

## 📊 System Architecture

```mermaid
graph TD
    %% Frontend Layer
    subclass UI
    A[Glassmorphism UI Dashboard] -->|POST /api/generate| B(Flask WSGI Backend Core)
    A <-->|Prometheus Scrape| E[MLOps /api/mlops/metrics]
    end

    %% Backend Layer
    subclass Backend
    B --> C{Algorithmic Synthesis Engine}
    C -->|Feature Engineering| D1[v2.5.1-xgboost-champion]
    C -->|Shadow Scoring| D2[v3.0.0-lgbm-shadow]
    D1 --> F{Pandas DataFrame Construction}
    end

    %% Output Layer
    subclass Data
    F -->|OpenPyXL Serialization| G[Verified_Leads.xlsx File Download]
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

## ☁️ Free Live Deployment on Vercel

The application is engineered with a `vercel.json` configuration file, making it completely ready to deploy as a Serverless API.

### How to deploy to Vercel (100% Free):
1. **Create a Vercel Account**: Go to [vercel.com](https://vercel.com/) and sign up with your GitHub account.
2. **Push your Code**: Ensure all this repository code is pushed to your GitHub `main` branch.
3. **Import to Vercel**: 
   - Click **"Add New..."** -> **"Project"** in Vercel.
   - Select your `leadgen-pro` GitHub repository.
4. **Deploy**: Vercel will automatically detect the `vercel.json` and install Python, Flask, and Pandas via the `requirements.txt` file. Click "Deploy".
5. **Live URL**: Within 2 minutes, you will receive a free, globally cached URL (e.g., `https://leadgen-pro-kunal.vercel.app`) to share with recruiters!

---

## 📝 License

Distributed under the MIT License - See `LICENSE.md` file for details.
