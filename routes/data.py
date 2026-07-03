from fastapi import FastAPI,APIRouter,Depends,UploadFile
import os 
from helpers.config import get_settings,Settings
from controllers import DataController
from models.enums import ResponseSignal
router=APIRouter(prefix="/api/v1/data",tags=["api_v1","data"])


@router.post("/upload/{product_id}")
async def upload_data(product_id:str,
                      file:UploadFile,
                      app_settings:Settings=Depends(get_settings)):
    # validate file type and size
    is_valid , signal =DataController().validate_upload_file(file)

    return {"is_valid":is_valid,
            "signal":signal
            }
