from fastapi import APIRouter, status, HTTPException
from .. import schemas, passutil, database


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=schemas.UserInfo, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.Signup):
    user.password = passutil.encrypt_password(user.password)
    try:
        database.cursor.execute("INSERT INTO users (user_name, email_address, password) VALUES (%s, %s, %s) RETURNING user_name, email_address", 
                                [user.username, user.email, user.password])
        new_user = database.cursor.fetchone()
        database.conn.commit()
        return new_user

    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, {"details":"username or email already exists!"})