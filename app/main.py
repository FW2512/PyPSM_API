from fastapi import FastAPI
from .routers import users, set_machine_info, get_machine_info, get_machine_status, set_machine_status, get_screenshots, set_screenshots

app = FastAPI(
    title="PyPSM",
    version="3.0.0",
    description="this API created for PyPSM which a software for monitor and manage your PC remotely from PyPSM android app",
    contact={"GitHub": "https://github.com/FW2512",
             "Telegram": "https://t.me/FirasJarmakani",
             "Gmail": "firasjarmakani@gmail.com"}
)
app.include_router(users.router)
app.include_router(set_machine_info.router)
app.include_router(get_machine_info.router)
app.include_router(get_machine_status.router)
app.include_router(set_machine_status.router)
app.include_router(get_screenshots.router)
app.include_router(set_screenshots.router)


@app.get("/")
def root():
    return {
        "message": "welcome to PyPSM API!", 
        "description": "this API created for PyPSM which a software for monitor and manage your PC remotely from PyPSM android app", 
        "developed_by": "FirasJarmakani",
        "contact_info":
            {
                "GitHub": "https://github.com/FW2512",
                "Telegram": "https://t.me/FirasJarmakani",
                "Gmail": "firasjarmakani@gmail.com"
            }
            }
