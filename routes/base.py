from fastapi import FastAPI ,APIRouter,Depends
import os
from helpers.config import get_settings,Settings
route=APIRouter(prefix="/api/v1",tags=["api_v1"])


@route.get("/") 
async def welcome(app_settings:Settings=Depends(get_settings)):
  
    app_name =app_settings.APP_NAME
    app_v=app_settings.APP_VERSION

    return{
        "message":"welcome Abdelrahman  to my API",
        "app_name": app_name,
        "app_version": app_v
    }