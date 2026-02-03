import joblib
from flask import jsonify, request

model = joblib.load("model.pkl")

def predict(request):
    """
    HTTP Cloud Function
    Expects JSON input with iris features
    """
    data = request.get_json(silent=True)

    required = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    if not data or any(k not in data for k in required):
        return jsonify({
            "error": "Missing required fields",
            "required_fields": required
        }), 400

    x = [[
        float(data["sepal_length"]),
        float(data["sepal_width"]),
        float(data["petal_length"]),
        float(data["petal_width"])
    ]]

    pred = model.predict(x)[0]
    return jsonify({"prediction": int(pred)})
