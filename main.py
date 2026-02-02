"""
Docstring for main

This is the API that will enable us better interact with the
LLMs that will generate a description for the specific holiday
in the specific country of interest.


"""
from fastapi import FastAPI
from dotenv import load_dotenv
from freeflow_llm import FreeFlowClient

load_dotenv()

app = FastAPI()

@app.get('/')
async def index():
    with FreeFlowClient() as client:
        return {"providers": client.list_providers()}
