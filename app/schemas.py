import email
from lib2to3.pytree import Base
from pydantic import BaseModel, EmailStr
import email_validator

class Signup(BaseModel):
    username: str
    email: EmailStr
    password: str


class login(BaseModel):
    username: EmailStr
    password: str


class UserInfo(BaseModel):
    user_name: str
    email_address: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None
    user_name : str


class SetMachineInfo(BaseModel):
    machine_name: str | None
    platform: str | None
    platform_version: str | None
    cpu_info: str | None
    battery_info: str | None
    ram_info: str | None

class GetMachineInfo(BaseModel):
    user_id: int 
    machine_name: str | None
    platform: str | None
    platform_version: str | None
    cpu_info: str | None
    battery_info: str | None
    ram_info: str | None

class GetMachineStatus(BaseModel):
    user_id: int
    online: bool | None = None
    shutdown: bool | None = None

class SetMachineStatus(BaseModel):
    online: bool | None = None
    shutdown: bool | None = None
    
class GetScreenshots(BaseModel):
    user_id: int
    take_shot: bool | None = True
    shot_base64: str | None

class SetScreenshots(BaseModel):
    take_shot: bool | None = False
    shot_base64: str | None = None

