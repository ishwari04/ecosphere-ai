
# Ecosphere-ai
AI-powered sustainability platform for route optimization and fossil fuel awareness

<h1 align="center">🌍 EcoSphere.ai</h1>
<h3 align="center">AI-Powered CO₂ Route Optimization & Fossil Fuel Awareness Platform</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-brightgreen.svg" />
  <img src="https://img.shields.io/badge/ML%20Models-RandomForest%20%7C%20XGBoost-orange.svg" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" />
  <img src="https://img.shields.io/badge/Status-Prototype%20v1.0-yellow.svg" />
</p>

---

## 🚀 Overview
**EcoSphere.ai** is an AI-driven sustainability platform designed to **minimize CO₂ emissions**, reduce **fuel costs**, and promote **fossil fuel awareness** in logistics and transportation.  
It uses **Machine Learning**, **Smart Routing Algorithms**, and an **interactive dashboard** to help companies achieve sustainability targets and align with **NetZero**, **ESG**, and **UN SDG** goals.

> “Optimizing Today, Sustaining Tomorrow.”

---

## 🧠 Model Summary — CO₂ Emission Prediction Engine
The **EcoSphere.ai CO₂ Emission Prediction Model** estimates the carbon output of logistics vehicles using real-world parameters such as vehicle type, fuel type, mileage, load weight, vehicle age, and maintenance efficiency.  
Built with **Random Forest** and **XGBoost**, it captures non-linear relationships between these inputs and emission levels, achieving an accuracy of **R² ≈ 0.99** on test data.

The model is trained on enriched and synthetically augmented datasets reflecting diverse trip conditions.  
It predicts emissions in **grams per kilometer**, providing interpretable, data-driven insights for logistics optimization, policy analysis, and ESG reporting.  
Deployed via **Streamlit**, users can interactively input trip details and obtain instant emission estimates — enabling smarter, sustainable transportation decisions that align with **NetZero** and **SDG** goals. 🌱

---

## 🌱 Core Concept
The logistics sector contributes significantly to global CO₂ emissions due to inefficient routing and fossil fuel dependency.  
EcoSphere.ai addresses this through two integrated modules:

1. 🔹 **CO₂ Route Optimization Engine** – Predicts and reduces emissions using ML.  
2. 🔹 **Fossil Fuel Countdown Dashboard** – Visualizes resource depletion and renewable transition trends.

Together, they form a **holistic sustainability ecosystem** for operational efficiency and climate awareness.

---

## ⚙️ System Architecture

### 🧠 1. CO₂ Emission Tracker (AI/ML)
Predicts emissions based on:
- Distance, Vehicle Type, Fuel Efficiency, Load Weight, Weather, and Road Condition  

**ML Models Used:**
- Linear Regression (baseline)  
- RandomForest Regressor *(final model)*  
- XGBoost (comparison)*  

**Formula**
```math
Emission(kg CO₂) = Distance(km) × Fuel Efficiency × Emission Factor(kg CO₂/L)
````

**Metrics:** R², MAE, RMSE

---

### 🗺️ 2. Smart Route Optimization

Multi-objective optimization using:

* **Dijkstra’s / A*** algorithms
* **Emission-cost tradeoff** models

**Output:** Optimized route with % CO₂ savings vs default routes.

---

### 🔥 3. Fossil Fuel Countdown Module

An awareness-driven simulation that visualizes **fossil fuel depletion** timelines.

**Features**

* Countdown timers for oil, gas, and coal reserves
* Interactive EV adoption and renewable sliders
* Real-time depletion projections

**Example Output**

> “At current rates, global oil reserves deplete in ~48 years.
> Increasing EV adoption by 30% extends it by 5+ years.”

---

### 📊 4. Dashboard & Reports

Built with **Streamlit**, featuring:

* Route comparison visualizations
* CO₂ prediction outputs
* Fossil fuel awareness charts
* ESG/BRSR-ready **PDF sustainability reports**

> **Next Upgrade:** React + Plotly dashboard and dual-cloud (AWS + Azure) deployment.

---

## 🧠 Detailed Model Description

### 🌍 Project Context

The **EcoSphere.ai** system predicts **carbon dioxide (CO₂) emissions** from logistics vehicles using AI.
It forms the analytical backbone of the EcoSphere.ai platform, enabling data-driven emission analysis, route optimization, and sustainability decision-making.

### ⚙️ Model Objective

To predict the **CO₂ emission rate (grams/km)** based on real-world features:

* Vehicle type, fuel type, mileage, load weight, age, and maintenance score.

### 🧩 Input Features

| Feature                | Description                                     | Type        |
| ---------------------- | ----------------------------------------------- | ----------- |
| vehicle_type           | Type of vehicle (Car/Truck)                     | Categorical |
| fuel_type              | Petrol, Diesel, Natural Gas, Ethanol, or EV     | Categorical |
| mileage_kmpl           | Vehicle mileage (km/litre)                      | Numeric     |
| load_weight            | Cargo weight (kg)                               | Numeric     |
| emission_factor        | Standard CO₂ per litre (e.g., Petrol 2.31 kg/L) | Numeric     |
| vehicle_age            | Age of vehicle (years)                          | Numeric     |
| maintenance_efficiency | Maintenance score (0–1)                         | Numeric     |

### 🔢 Output Variable

| Feature      | Description                        |
| ------------ | ---------------------------------- |
| co2_emission | Predicted CO₂ emission in grams/km |

### 💡 Model Flow

1. Physics-based baseline:
   [
   CO₂ = \frac{Distance}{Mileage} × EmissionFactor
   ]
2. Adjusted using real-world modifiers: vehicle age, load, and maintenance.
3. Synthetic data generation ensures robust model training.
4. RandomForest and XGBoost are trained; **RandomForest achieves R² ≈ 0.99**.
5. Model deployed with **joblib** for real-time prediction in Streamlit UI.

### 📊 Evaluation

| Metric | Meaning                        | Result           |
| ------ | ------------------------------ | ---------------- |
| R²     | Model fit accuracy             | 0.991            |
| MAE    | Avg. absolute prediction error | ~9 g/km          |
| RMSE   | Penalizes large errors         | Low (consistent) |

---

## 🧰 Tech Stack

| Category                 | Tools & Technologies                                            |
| ------------------------ | --------------------------------------------------------------- |
| **Language**             | Python                                                          |
| **Libraries**            | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost       |
| **Visualization**        | Streamlit, Plotly                                               |
| **Algorithms**           | Dijkstra’s / A*, Multi-Objective Optimization                   |
| **Deployment (Planned)** | AWS, Azure                                                      |
| **Reporting**            | FPDF / ReportLab                                                |
| **Dataset Sources**      | Our World in Data, IEA, OpenStreetMap, Google Maps API, co2.csv |

---

## 🧪 Workflow

```mermaid
flowchart TD
A[Data Collection] --> B[Preprocessing & Feature Engineering]
B --> C[Model Training (Random Forest, XGBoost)]
C --> D[Emission Prediction & Route Optimization]
D --> E[Dashboard Visualization]
E --> F[ESG/BRSR Report Generation]
```

---

## 📈 Results

* **Model Accuracy:** R² ≈ 0.99 (Random Forest)
* **Emission Savings:** 8–15% on optimized routes
* **Interactive Dashboard:** Real-time emission prediction & awareness module

---

## 💡 Innovation & Differentiation

| Traditional Tools                        | EcoSphere.ai                          |
| ---------------------------------------- | ------------------------------------- |
| Route optimization only by distance/time | Adds CO₂, fuel, and cost intelligence |
| Static calculators                       | Predictive ML models                  |
| One-way reports                          | Interactive dashboard                 |
| No ESG/BRSR link                         | Compliance-ready outputs              |

---

## 🔭 Future Enhancements

* Reinforcement Learning for adaptive routing
* Regional-level fossil depletion forecasts
* Enterprise-grade React dashboard
* AWS + Azure cloud deployment
* Real-time data sync via ERP & IoT

---

## 🌍 Use Cases

* **Logistics Firms** → Optimize delivery routes, minimize emissions
* **Corporate ESG Teams** → Generate sustainability reports
* **Governments & NGOs** → Monitor fossil fuel trends
* **Public Awareness Campaigns** → Engage via visual dashboards

---

## 📁 Repository Structure

```
EcoSphere.ai/
│
├── AIML_CO2_PROJECT.ipynb     # Model & training pipeline
├── co2.csv                    # Dataset
├── report/                    # Project documentation
├── app/                       # Streamlit dashboard
├── requirements.txt            # Dependencies
└── README.md                   # Overview
```

---

## ⚙️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/EcoSphere.ai.git
cd EcoSphere.ai

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run Notebook
jupyter notebook AIML_CO2_PROJECT.ipynb

# 4️⃣ Launch Dashboard
streamlit run app.py
```

---

## 🏁 Conclusion

**EcoSphere.ai** merges AI innovation with environmental intelligence to optimize logistics and promote sustainable energy awareness.
By predicting emissions, optimizing routes, and visualizing fossil depletion trends, it helps organizations achieve measurable climate goals.

> 🌿 *Empowering logistics for a greener, smarter, and fossil-free tomorrow.*

---

## 👥 Contributors

| Name                           | Role                            |
| ------------------------------ | ------------------------------- |
| **Ishwari Kakade**             | Lead Developer & ML Architect   |
| **Kritika Nimje**              | Data Analyst & Model Validation |
| **Atharva Kale**               | Visualization & Research        |
| **Mentor:** *Dr. Princy Diwan* | Project Guide                   |

---

## 🔗 References

* [Our World in Data – CO₂ & Energy Statistics](https://ourworldindata.org/co2-and-greenhouse-gas-emissions)
* [Google Maps API](https://developers.google.com/maps/documentation)
* [IEA Reports](https://www.iea.org/reports)
* [Streamlit Docs](https://docs.streamlit.io/)

---

<p align="center">
  Made with ❤️ by <b>Ishwari Kakade</b><br/>
  <i>AI-ML Specialization Project | 2025</i>
</p>
```


Would you like me to generate the matching **`requirements.txt`** file now (with all Python dependencies used in your notebook and Streamlit app)?
