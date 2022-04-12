from datetime import datetime, timedelta
from jose import jwt, JWTError
from . import schemas, config
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
# openssl rand -hex 32
SECRET_KEY = config.settings.secret_key
ALGORITHM = config.settings.algorithm
EXPIRATION_TIME = config.settings.expiration_time

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


def create_jwt_token(data: dict):
    to_encode = data.copy()
    exp = datetime.utcnow() + timedelta(minutes=EXPIRATION_TIME)
    to_encode.update({"exp": exp})
    
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id: str = payload.get("id")
        user_name: str = payload.get("email")
        if not id or not user_name:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate", headers={"WWW-AUTHENTICATE": "Bearer"})
        token_data = schemas.TokenData(id = id, user_name=user_name)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate", headers={"WWW-AUTHENTICATE": "Bearer"})

    return token_data 

def get_current_user(token: str = Depends(oauth2_schema)):
    return verify_jwt_token(token)