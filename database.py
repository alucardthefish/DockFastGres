from operator import imod
import os, sys
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASEDIR:", BASE_DIR)
# load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv(find_dotenv())
sys.path.append(BASE_DIR)
print("path that load env file:", os.path.join(BASE_DIR, ".env"))
print("Path that was finding .env:", find_dotenv())
print("os.environ:", os.environ["DATABASE_URL"])

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]


engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()