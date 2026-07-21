import joblib


# Load trained model
model = joblib.load("iris_model.pkl")


# New flower measurements
flower = [
    [
        5.1,  # sepal length
        3.5,  # sepal width
        1.4,  # petal length
        0.2   # petal width
    ]
]


# Prediction
prediction = model.predict(flower)


classes = [
    "Setosa",
    "Versicolor",
    "Virginica"
]


print("Prediction:", classes[prediction[0]])