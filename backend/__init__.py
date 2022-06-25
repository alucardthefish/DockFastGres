import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(find_dotenv(".env"))
db_session = db

def create_app():
    app = FastAPI(
        title="My API",
        description="Simple rest-full api with postgres",
        version="1.0"
    )
    return app

def init_app(app: FastAPI):
    app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
    return app
