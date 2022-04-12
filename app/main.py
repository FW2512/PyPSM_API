from fastapi import FastAPI
from .routers import users, set_machine_info, get_machine_info

app = FastAPI()
app.include_router(users.router)
app.include_router(set_machine_info.router)
app.include_router(get_machine_info.router)


@app.get("/")
def root():
    return {"message": "welcome to PyPSM API!", 
            "description": "this API created for PyPSM which a software for monitor and manage your PC remotely from PyPSM android app", 
            "developed_by": "FirasJarmakani",
            "contact_info":"more details will be available soon"}
