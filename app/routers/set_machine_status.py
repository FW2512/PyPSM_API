from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, oauth2


router = APIRouter(prefix="/machinestatus", tags=["Machine Status"])


@router.put("/setstatus", response_model=schemas.GetMachineStatus)
def set_status(machine_status: schemas.SetMachineStatus, current_user=Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", [current_user.id])
    recived_info = database.cursor.fetchone()
    if recived_info:
        database.cursor.execute("""UPDATE machine_status SET online = %s, shutdown = %s WHERE user_id = %s RETURNING *""",
                                [machine_status.online, machine_status.shutdown, current_user.id])
        sent_data = database.cursor.fetchone()
        database.conn.commit()
        return sent_data
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Unauthorized submition!")