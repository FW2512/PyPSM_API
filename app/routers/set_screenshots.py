from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, oauth2


router = APIRouter(prefix="/screenshots", tags=["Screenshots"])


@router.put("/setscreenshots", response_model=schemas.SetScreenshots)
def set_status(screenshot: schemas.SetScreenshots, current_user=Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", [current_user.id])
    recived_info = database.cursor.fetchone()
    if recived_info:
        database.cursor.execute("""UPDATE screenshots SET take_shot = %s, shot_base64 = %s WHERE user_id = %s RETURNING *""",
                                [screenshot.take_shot, screenshot.shot_base64, current_user.id])
        sent_data = database.cursor.fetchone()
        database.conn.commit()
        return sent_data
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Unauthorized submition!")