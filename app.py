import pickle
from flask import Flask, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/predict", methods=["POST"])
def predict():
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    
    if year is None or month is None:
        return {"error": "Missing input value"}, 400
    elif year < 2022:
        return {"error": "Select a year in the future"}, 400
    elif month < 1 or month > 12:
        return {"error": "Invalid month"}, 400
    else:
        features = [0, 1, year, month]
        prediction = model.predict([features])
        return {"prediction": prediction}, 200
    
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
