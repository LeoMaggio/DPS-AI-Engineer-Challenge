import pickle
from fastapi import FastAPI, responses
from pydantic import BaseModel

app = FastAPI()
model = pickle.load(open('./model.pkl', 'rb'))

class Item(BaseModel):
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
        return responses.JSONResponse({"error": "Missing input value"})
    elif year < 2022:
        return responses.JSONResponse({"error": "Select a year in the future"})
    elif month < 1 or month > 12:
        return responses.JSONResponse({"error": "Invalid month"})
    else:
        target = [0, 1, year, month]
        prediction = model.predict([features])
        return responses.JSONResponse({'prediction': prediction[0]})
    
if __name__ == "__main__":
    uvicorn.run(app, host='93.34.148.69', port=int(os.environ.get('PORT', 5000)))
