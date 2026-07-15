from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from preprocess import preprocess

app = Flask(__name__)
CORS(app)

# Load saved model and vectorizer
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


@app.route("/")
def home():
    return "Spam Detection API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data["message"]

    # Preprocess input
    cleaned_message = preprocess(message)

    # Convert to vector
    message_vector = vectorizer.transform([cleaned_message])

    # Predict
    prediction = model.predict(message_vector)[0]

    result = "spam" if prediction == 1 else "ham"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)