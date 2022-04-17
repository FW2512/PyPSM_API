from fastapi import APIRouter, HTTPException, status, Depends

from app import schemas
from .. import database, oauth2


router = APIRouter(prefix="/machineinfo", tags=["Machine Information"])

@router.get("/getinfo", response_model=schemas.GetMachineInfo)
def getinfo(current_user = Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", [current_user.id])
    user_info = database.cursor.fetchone()
    if user_info:
        database.cursor.execute("SELECT * FROM users LEFT JOIN machine_info ON machine_info.user_id = users.user_id WHERE users.user_id = %s;", [current_user.id])
        machine_info = database.cursor.fetchone()
        return machine_info

    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

@router.get("/getstatus", response_model=schemas.MachineStatus)
def get_status(current_user = Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", [current_user.id])
    user_info = database.cursor.fetchone()
    if user_info:
        database.cursor.execute("SELECT * FROM users LEFT JOIN machine_status ON machine_status.user_id = users.user_id WHERE users.user_id = %s;", [current_user.id])
        machine_status = database.cursor.fetchone()
        return machine_status

    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)