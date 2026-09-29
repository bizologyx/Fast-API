from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Fast API is working"}

@app.get("/about")
def about():
    return {"About me": "Hey I'm Hashir Shahid", "Project":"This is my first FastAPI Project", "Expression":"Hurrayyyyyyy"}

@app.get("/contact")
def contact():
    return {"Name":"Hashir Shahid", "Number":"0300-xxxxx", "Age":18, "Degree":"BS Computer Science"}