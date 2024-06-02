import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()
load_dotenv()


# Фиксированные пользователи с их паролями
users = {
    os.getenv('BASIC_USER_LOGIN'): os.getenv('BASIC_USER_PASSWORD'),
    os.getenv('ADMIN_USER_LOGIN'): os.getenv('ADMIN_USER_PASSWORD')

}


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    for correct_username, correct_password in users.items():
        if credentials.username == correct_username and credentials.password == correct_password:
            return credentials.username
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
