# Script to generate the titanic_sample.csv dataset
# Run this first before running any other part

import pandas as pd
import numpy as np

np.random.seed(42)
n = 600

ages = np.clip(np.random.normal(30, 14, n), 0.5, 80).round(1).astype(object)
for i in np.random.choice(n, int(n*0.15), replace=False):
    ages[i] = None

fares = np.clip(np.random.exponential(32, n), 4, 512).round(2).astype(object)
for i in np.random.choice(n, 10, replace=False):
    fares[i] = None

embarked = np.random.choice(["S","C","Q"], n, p=[0.72,0.19,0.09]).astype(object)
for i in np.random.choice(n, 5, replace=False):
    embarked[i] = None

df = pd.DataFrame({
    "PassengerId": range(1, n+1),
    "Survived": np.random.choice([0, 1], n, p=[0.62, 0.38]),
    "Pclass": np.random.choice([1, 2, 3], n, p=[0.24, 0.21, 0.55]),
    "Name": ["Passenger_" + str(i) for i in range(1, n+1)],
    "Sex": np.random.choice(["male", "female"], n, p=[0.65, 0.35]),
    "Age": ages,
    "SibSp": np.random.choice([0,1,2,3,4,5], n, p=[0.68,0.23,0.05,0.02,0.01,0.01]),
    "Parch": np.random.choice([0,1,2,3], n, p=[0.77,0.13,0.08,0.02]),
    "Fare": fares,
    "Embarked": embarked
})

df.to_csv("titanic_sample.csv", index=False)
print(f"Dataset generated: {df.shape[0]} rows x {df.shape[1]} columns")
print("Saved as titanic_sample.csv")
