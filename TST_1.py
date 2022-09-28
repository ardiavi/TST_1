from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mahasiswa(BaseModel):
    NIM : str
    Nama: str

data_mahasiswa = {}

@app.get("/")
async def root():
    return {"Page": "Root"}

@app.get("/get-data")
def get_all_data():
    return data_mahasiswa

@app.post("/add-mahasiswa")
def add_mahasiswa(mahasiswa: Mahasiswa) :
    id = len(data_mahasiswa)+1
    data_mahasiswa[id] = mahasiswa
    return data_mahasiswa[id]
