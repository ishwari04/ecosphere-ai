# ecosphere-ai
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
