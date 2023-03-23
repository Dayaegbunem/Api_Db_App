from fastapi import FastAPI
from pydantic import BaseModel
import pymongo
import urllib.parse
import json
from bson import json_util
import json


class Item(BaseModel):
    name: str
    age: int
    city: str
    company: str


cluster = pymongo.MongoClient("mongodb+srv://"+urllib.parse.quote_plus('Dayaegbunem')+":"+urllib.parse.quote_plus('zYqp7wmUXx2nBZV0')+"@cluster0.yysevdx.mongodb.net/?retryWrites=true&w=majority")
db = cluster["ecom"]
collection = db["ecom"]

app = FastAPI()



@app.post("/create/")
def create(item: Item):
    collection.insert_one({"name":item.name,"city":item.city,"age":item.age,"company":item.company})
    return item



@app.get("/find/{name}")
def find(name: str):
    result=collection.find_one({"name":name})
    result=json.loads(json_util.dumps(result))
    return  result


@app.put("/update/{name}")
def update(name: str,data:dict):
    try:
        collection.update_one({"name":name},{"$set": data})
        return {"status":"successfully updated"}
    except Exception as e:
        print(e)



@app.delete("/delete/{name}")
def delete(name: str):
    try:
        collection.delete_one({"name":name})
        return {"status":"successfully deleted"}
    except Exception as e:
        print(e)