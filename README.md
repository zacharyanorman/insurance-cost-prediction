# Insurance Cost Prediction

This project explores healthcare charges using the Medical Cost Personal Dataset (from Kaggle).  
I built multiple linear regression models in Python to predict insurance costs based on patient characteristics such as age, BMI, number of children, sex, and smoking status.

---

## Dataset
- Source: [Kaggle – Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)  
- 1,338 patient records with the following features:
  - `age`: age of the beneficiary  
  - `sex`: male or female  
  - `bmi`: body mass index  
  - `children`: number of dependents covered by insurance  
  - `smoker`: yes/no  
  - `region`: (not used in final model)  
  - `charges`: medical insurance cost (target variable)  

---

## Methods
- Preprocessed categorical variables (encoded `sex` and `smoker`)  
- Engineered interaction terms:
  - `smoker × bmi` → strongest cost driver  
  - `smoker × age` → tested but weaker  
- Added polynomial features (`age²`) to capture nonlinear effects  
- Compared raw-cost vs. log-transformed models  
- Evaluated fit using R², adjusted R², residual analysis, and diagnostic plots

---

## Results
- Baseline model (no interactions): R² ≈ 0.75  
- With interactions: R² ≈ 0.84  
- Log-transformed model: R² ≈ 0.81, more stable residuals and interpretable as percentage changes  
- Key insights:
  - Smokers’ costs are ~250% higher on average than non-smokers  
  - BMI strongly increases charges only for smokers (interaction effect)  
  - Age² shows accelerating cost increases with age  
  - Sex is not a strong predictor after adjusting for other variables  

---

## Visuals
The project includes:
- Predicted vs. Actual charges  
- Residual plots (raw vs. log scale)  
- Feature importance analysis from regression coefficients  

---

## Tech Stack
- Python (pandas, numpy, statsmodels, matplotlib)  
- VS Code  
- Git & GitHub for version control  

---

## How to Run
1. Clone this repo:  
   ```bash
   git clone https://github.com/yourusername/insurance-cost-prediction.git
   cd insurance-cost-prediction
