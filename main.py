from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

#carrega os arquivos da variavel de ambiente(ex: .env)
load_dotenv()
#encontra o a secret key e carrega ela
Key_crypt = os.getenv("Key_crypt")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)