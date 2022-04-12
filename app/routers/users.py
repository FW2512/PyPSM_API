from fastapi import APIRouter, status, HTTPException
from .. import schemas, passutil, database, oauth2


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup", response_model=schemas.UserInfo, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.Signup):
    user.password = passutil.encrypt_password(user.password)
    try:
        database.cursor.execute("INSERT INTO users (user_name, email_address, password) VALUES (%s, %s, %s) RETURNING user_id, user_name, email_address", 
                                [user.username, user.email, user.password])
        new_user = database.cursor.fetchone()
        database.cursor.execute("INSERT INTO machine_info (user_id) VALUES (%s)", [new_user["user_id"]])
        database.conn.commit()
        return new_user

    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, {"details":"username or email already exists!"})


@router.post("/login", response_model=schemas.Token)
def login(user_info: schemas.login):
    database.cursor.execute("SELECT user_id, email_address, password FROM users WHERE email_address = %s", [user_info.email])
    recived_user_info = database.cursor.fetchone()
    if recived_user_info:
        if passutil.password_validation(user_info.password, recived_user_info["password"]):
            access_token = oauth2.create_jwt_token({"id": recived_user_info.get("user_id"), 
                                     "email": recived_user_info.get("email_address")})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invaild password!")
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="email address not found!")