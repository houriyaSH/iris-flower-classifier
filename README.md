# 🌸 Iris Flower Classifier

A Machine Learning web application that predicts the species of an Iris flower based on four botanical measurements.

The project uses a trained Machine Learning model deployed as a Flask web application.

---

## 🚀 Demo

The application allows users to enter:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

and predicts the Iris species instantly.

---

## 🧠 Machine Learning

The model was trained using the Iris dataset.

Features:

- SepalLengthCm
- SepalWidthCm
- PetalLengthCm
- PetalWidthCm

Target:

- Species

Machine Learning algorithm:

- Scikit-learn Classification Model

---

## 🛠 Technologies Used

### Backend

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```text
iris-project

├── app.py
├── model.py
├── Iris.csv
├── iris_model.pkl
├── requirements.txt

├── templates
│   └── index.html

├── static
│   ├── style.css
│   └── script.js

├── test_api.py
├── test_model.py

└── .gitignore
```



## ⚙️ How To Run The Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/houriyaSH/iris-flower-classifier.git
```

### 2. Go to project directory

```bash
cd iris-flower-classifier
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Flask application

```bash
python app.py
```

### 7. Open browser

```
http://127.0.0.1:5000
```
## 🔍 Example Prediction
Example input:
Example Prediction
Example input:
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2


## Model output:
Iris-setosa

## 🧪 Testing

The project includes test files:

test_model.py
test_api.py

The model was tested successfully and returned correct predictions.

## 🚀 Current Status

- ✅ Dataset loaded
- ✅ Machine Learning model trained
- ✅ Model saved as .pkl file
- ✅ Flask API created
- ✅ Frontend designed
- ✅ API connected to frontend
- ✅ Project uploaded to GitHub

🔮 Future Improvements

Possible future updates:

- Deploy the application online
- Improve UI design
- Add prediction history
- Add more Machine Learning models
- Add charts and data visualization

## 👨‍💻 Author

Created by Houriya

Machine Learning deployment project built using Python, Flask, and Scikit-learn.
