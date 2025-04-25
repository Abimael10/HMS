# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------
# 🔗 API URL CONFIG
# ------------------------------

def get_api_url() -> str:
    # Puedes setear esto como variable de entorno o usar por defecto localhost
    return os.getenv("API_URL")


# ------------------------------
# 🛢️ POSTGRES URI CONFIG
# ------------------------------

def get_postgres_uri() -> str:
    return os.getenv("POSTGRES_URI")