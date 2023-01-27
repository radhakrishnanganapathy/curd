from fastapi import FastAPI 
# from route import router
from app.api import api_router
from app.db import database
from fastapi.middleware.cors import CORSMiddleware
from app import config
app=FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.CreateTables()

@app.get('/')
def home():
	return ("i am alive")

app.include_router(api_router)	