import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from backend.api import API_TAGS_METADATA


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(find_dotenv(".env"))

def create_app():
    app = FastAPI(
        title="My ASYNC API",
        description="Simple rest-full api with postgres",
        version="1.0",
        openapi_tags=API_TAGS_METADATA
    )
    return app
