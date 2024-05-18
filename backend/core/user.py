import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

load_dotenv()

app = FastAPI()

security = HTTPBasic()

# Фиксированные пользователи с их паролями
users = {
    "basic_user": os.getenv('BASIC_USER_PASSWORD'),
    "admin_user": os.getenv('ADMIN_USER_PASSWORD')
}


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    password = users.get(credentials.username)
    if not password or credentials.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
