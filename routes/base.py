from fastapi import FastAPI ,APIRouter
import os
route=APIRouter(prefix="/api/v1",tags=["api_v1"])


@route.get("/") 
async def welcome():
    app_name =os.getenv("APP_NAME")
    app_v=os.getenv("APP_VERSION")
    return{
        "message":"welcome Abdelrahman  to my API",
        "app_name": app_name,
        "app_version": app_v
    }