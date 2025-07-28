from fastapi import FastAPI

app = FastAPI()

#GET endpoint

@app.get('/')
def read_root():
    return {"message":"Hello, FastAPI!"}

@app.post("/submit")
def submit_data(data: dict):
    return{"received":data}