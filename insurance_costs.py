import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('insurance.csv')

X = df[['age^2', 'sex', 'bmi', 'children', 'smoker', 'smoker x age', 'smoker x bmi']]
X = sm.add_constant(X)

y = np.log(df["charges"])

model = sm.OLS(y, X).fit()

print(model.summary())

predictions = model.predict(X)
residuals = y - predictions  # both in log space

# 1. Predicted vs. Actuals

predictions_dollars = np.exp(model.predict(X))

plt.scatter(df["charges"], predictions_dollars, alpha=0.5)
plt.plot([df["charges"].min(), df["charges"].max()],
         [df["charges"].min(), df["charges"].max()],
         color="red", linestyle="--")

plt.xlabel("Actual Charges ($)")
plt.ylabel("Predicted Charges ($)")
plt.title("Predicted vs. Actual Charges (Back-transformed)")

plt.show()

# 2. Residuals vs Predicted

plt.scatter(predictions, residuals, alpha=0.5)
plt.axhline(0, color="red", linestyle="--")

plt.xlabel("Predicted log(Charges)")
plt.ylabel("Residuals (log scale)")
plt.title("Residuals vs. Predicted (Log Scale)")

plt.show()

zack_norman = pd.DataFrame([{
    "const": 1,
    "age^2": 32**2,
    "sex": 1,
    "bmi": 25,
    "children": 0,
    "smoker": 0,
    "smoker x age": 0,
    "smoker x bmi": 0}])

log_predict_zack = model.predict(zack_norman)[0]
charges_predicted = np.exp(log_predict_zack)
predicted_monthlty_charges = charges_predicted/12
print(f"Zack should be paying ${predicted_monthlty_charges:.2f} a month for insurance")

rachel_shapiro = pd.DataFrame([{
    "const": 1,
    "age^2": 34**2,
    "sex": 0,
    "bmi": 23,
    "children": 0,
    "smoker": 0,
    "smoker x age": 0,
    "smoker x bmi": 0}])

log_predict_rachel = model.predict(rachel_shapiro)[0]
weef_charges = np.exp(log_predict_rachel)
predicted_weef_charges = weef_charges/12
print(f"Weef should be paying ${predicted_weef_charges:.2f} a month for insurance")

tony_whiddon = pd.DataFrame([{
    "const": 1,
    "age^2": 60**2,
    "sex": 1,
    "bmi": 24,
    "children": 2,
    "smoker": 0,
    "smoker x age": 0,
    "smoker x bmi": 0}])

log_predict_tony = model.predict(tony_whiddon)[0]
tony_charges = np.exp(log_predict_tony)
predicted_tony_charges = tony_charges/12
print(f"Uncle Tony should be paying ${predicted_tony_charges:.2f} a month for insurance")

mark_norman = pd.DataFrame([{
    "const": 1,
    "age^2": 64**2,
    "sex": 1,
    "bmi": 20,
    "children": 2,
    "smoker": 1,
    "smoker x age": 64,
    "smoker x bmi": 20}])

log_predict_mark = model.predict(mark_norman)[0]
mark_charges = np.exp(log_predict_mark)
predicted_mark_charges = mark_charges/12
print(f"Dad should be paying ${predicted_mark_charges:.2f} a month for insurance")

print(mark_charges)