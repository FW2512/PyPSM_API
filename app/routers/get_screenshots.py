from fastapi import APIRouter, HTTPException, status, Depends

from app import schemas
from .. import database, oauth2


router = APIRouter(prefix="/screenshots", tags=["Screenshots"])


@router.get("/getscreenshots", response_model=schemas.GetScreenshots)
def getinfo(current_user = Depends(oauth2.get_current_user)):
    database.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", [current_user.id])
    user_info = database.cursor.fetchone()
    if user_info:
        database.cursor.execute("SELECT * FROM users LEFT JOIN screenshots ON screenshots.user_id = users.user_id WHERE users.user_id = %s;", [current_user.id])
        screenshot = database.cursor.fetchone()
        return screenshot
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)