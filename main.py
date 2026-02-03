"""
Docstring for main

This is the API that will enable us better interact with the
LLMs that will generate a description for the specific holiday
in the specific country of interest.


"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from freeflow_llm import FreeFlowClient, RateLimitError

load_dotenv()

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*']
)

@app.get('/')
async def index():
    with FreeFlowClient() as client:
        return {"providers": client.list_providers()}

@app.get('/countries/{country_name}/holidays/{holiday_name}')
async def get_description(country_name: str, holiday_name: str):
    prompt = f'''Write a clear, culturally accurate essay (120-150 words) describing
    how {holiday_name} is observed in {country_name}, focusing on traditions, public activities,
    and the general atmosphere, using a friendly, neutral tone and avoiding politics.'''

    try:
        with FreeFlowClient() as client:
            response = client.chat(
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        return {"Response": response.content}
    except RateLimitError:
        return {"Error": "You've exceeded the limits of this resource."}
    except Exception:
        return {"Error": "Oops! something failed. Please try again"}
