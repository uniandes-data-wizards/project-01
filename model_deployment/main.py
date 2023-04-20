from typing import Optional

from fastapi import FastAPI

import pandas as pd

# import DataModel from the same folder
from DataModel import DataModel

from preprocessor import Preprocessor

from joblib import load


app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    print(df)
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    print(result)
    return result[0]
