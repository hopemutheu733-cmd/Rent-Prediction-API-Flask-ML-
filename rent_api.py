import pandas as pd
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression

homes = pd.DataFrame({
    "size_sqm": [20, 25, 30, 35, 40, 50, 60, 70],
    "rooms":    [1, 1, 2, 2, 3, 3, 4, 4],
    "rent":     [8000, 9500, 13000, 15000, 19000, 22000, 30000, 34000],
})
model = LinearRegression().fit(homes[["size_sqm", "rooms"]], homes["rent"])

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    row = pd.DataFrame([[data["size_sqm"], data["rooms"]]], columns=["size_sqm", "rooms"])
    rent = model.predict(row)[0]
    return jsonify({"predicted_rent": round(float(rent))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)