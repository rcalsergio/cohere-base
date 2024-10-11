from fastapi import FastAPI
from cohere_class import CohereGenerator

app = FastAPI()
co = CohereGenerator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/chat/{text}")
async def send(text: str):
    return co.ask(text)