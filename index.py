from fastapi import FastAPI
from routes.student import student


app = FastAPI()
app.include_router(student)


@app.get("/")
def home():
    return {"message": "Hello World"}
