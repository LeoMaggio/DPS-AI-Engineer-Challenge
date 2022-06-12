import pickle
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
model = pickle.load(open('./model.pkl', 'rb'))

@app.route("/", methods = ["GET","POST"])
def index():
    output = ""
    if request.method == "POST":
        year = request.form["year"]
        month = request.form["month"]
        output = pred.prediction(year, month)     

    return render_template("index.html", value=output)

@app.route("/predict", methods = ["POST"])
def predict():
    output = ""
    if request.method == "POST":
        year = request.json["year"]
        month = request.json["month"]
        if year is None or month is None:
            return {"error": "Missing input value"}, 400
        elif year < 2022:
            return {"error": "Select a year in the future"}, 400
        elif month < 1 or month > 12:
            return {"error": "Invalid month"}, 400
        else:
            target = [0, 1, year, month]
            prediction = model.predict([target])
            return jsonify({'prediction': prediction[0]})
    
if __name__ == "__main__":
    app.run(debug = True)
