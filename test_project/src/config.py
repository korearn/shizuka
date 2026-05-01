import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URL = os.getenv('DB_URL', 'sqlite:///local.db')
    LLM_API_URL = os.getenv('LLM_API_URL', 'http://localhost:1234/v1')
