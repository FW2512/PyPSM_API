from fastapi import FastAPI, APIRouter


app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to PyPSM API!", 
            "description": "this API created for PyPSM which a software for monitor and manage your PC remotely from PyPSM android app", 
            "developed_by": "FirasJarmakani",
            "contact_info":"more details will be available soon"}
