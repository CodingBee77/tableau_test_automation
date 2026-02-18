import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SERVER_URL = os.getenv("TABLEAU_SERVER_URL")
    SITE_ID = os.getenv("TABLEAU_SITE")
    PAT_NAME = os.getenv("TABLEAU_PAT_NAME")
    PAT_VALUE = os.getenv("TABLEAU_PAT_VALUE")
    USERNAME = os.getenv("TABLEAU_USERNAME")
    PASSWORD = os.getenv("TABLEAU_PASSWORD")
