# train_model_with_confusion.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, classification_report
import joblib

# 1. Load dataset
data = pd.read_csv("waste_data.csv")

# Features and target
X = data[["weight_kg", "item_count", "avg_moisture", "days_since_collection"]]
y = data["bin_fill_percent"]

# 2. Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Polynomial features (optional)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 4. Train regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 5. Predict
y_pred = model.predict(X_test_poly)

# 6. Convert regression outputs into categories
def categorize(value):
    if value < 30:
        return "Empty"
    elif value < 70:
        return "Moderate"
    else:
        return "Full"

y_test_cat = [categorize(v) for v in y_test]
y_pred_cat = [categorize(v) for v in y_pred]

# 7. Confusion matrix
cm = confusion_matrix(y_test_cat, y_pred_cat, labels=["Empty", "Moderate", "Full"])
print("Confusion Matrix:\n", cm)

# 8. Classification report
print("\nClassification Report:\n", classification_report(y_test_cat, y_pred_cat))

# 9. Save model + transformer
joblib.dump(model, "model.pkl")
joblib.dump(poly, "poly.pkl")
print("Training complete. Model and transformer saved.")
