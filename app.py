import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = pickle.load(open('./model.pkl', 'rb'))

class Item(BaseModel):
    MONATSZAHL: int
    AUSPRAEGUNG: int
    JAHR: int
    MONAT: int

@app.get("/")
async def root():
   return {"message": "Hello World"}

@app.post("/predict/")
async def predict(item: Item):
    item = item.dict()
    data = list(item.values())
    year = data[0]
    month = data[1]
    if year is None or month is None:
        return {"error": "Missing input value"}, 400
    elif year < 2022:
        return {"error": "Select a year in the future"}, 400
    elif month < 1 or month > 12:
        return {"error": "Invalid month"}, 400
    else:
        target = features = [0, 1, year, month]
        prediction = model.predict([features])
        return {'prediction': prediction[0]}, 200
    
if __name__ == "__main__":
    app.run("0.0.0.0", int(os.environ.get('PORT', 5000)))
