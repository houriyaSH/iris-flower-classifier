from flask import Flask, request, jsonify, render_template
import joblib


app = Flask(__name__)


# Load trained model
model = joblib.load("iris_model.pkl")



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.json


        features = [

            float(data["sepal_length"]),
            float(data["sepal_width"]),
            float(data["petal_length"]),
            float(data["petal_width"])

        ]


        prediction = model.predict([features])


        result = prediction[0]


        return jsonify({

            "prediction": result

        })


    except ValueError:


        return jsonify({

            "error": "Please enter numbers only"

        }), 400



    except Exception as e:


        return jsonify({

            "error": str(e)

        }), 500




if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)