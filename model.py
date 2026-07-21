import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# خواندن فایل CSV
data = pd.read_csv("Iris.csv")


# حذف ستون Id
data = data.drop("Id", axis=1)


# ورودی های مدل
X = data[
    [
        "SepalLengthCm",
        "SepalWidthCm",
        "PetalLengthCm",
        "PetalWidthCm"
    ]
]


# خروجی مدل
y = data["Species"]


# تقسیم داده
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ساخت مدل
model = RandomForestClassifier(random_state=42)


# آموزش
model.fit(X_train, y_train)


# پیش بینی
prediction = model.predict(X_test)


# محاسبه دقت
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)


# ذخیره مدل
joblib.dump(model, "iris_model.pkl")

print("Model saved successfully!")