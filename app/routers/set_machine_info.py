from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, oauth2

router = APIRouter(prefix="/machineinfo", tags=["Machine Information"])


@router.put("/setinfo", response_model=schemas.GetMachineInfo)
def set_info(machine_info: schemas.SetMachineInfo, current_user=Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM machine_info WHERE user_id = %s", [current_user.id])
    recived_info = database.cursor.fetchone()
    if recived_info:
        database.cursor.execute("""UPDATE machine_info SET machine_name = %s, platform = %s, platform_version = %s, cpu_info = %s, battery_info = %s, ram_info = %s WHERE user_id = %s RETURNING *""",
                                [machine_info.machine_name, machine_info.platform, machine_info.platform_version, machine_info.cpu_info, machine_info.battery_info, machine_info.ram_info, current_user.id])
        sent_data = database.cursor.fetchone()
        database.conn.commit()
        return sent_data
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Unauthorized submition!")

@router.put("/setstatus", response_model=schemas.MachineStatus)
def set_status(machine_status: schemas.MachineStatus, current_user=Depends(oauth2.get_current_user)):
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