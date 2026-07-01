from fastapi import FastAPI

app = FastAPI()

#endpoint de inicio

@app.get("/")
def inicio ():
    return {"mensaje": "Hola estoy aprendiendo FastAPI"}