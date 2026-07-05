from signal import signal

from fastapi import FastAPI,APIRouter,Depends,UploadFile,status
from fastapi.responses import JSONResponse
import os 
from helpers.config import get_settings,Settings
from controllers import DataController ,ProjectController
from models.enums import ResponseSignal
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')

router=APIRouter(prefix="/api/v1/data",tags=["api_v1","data"])


@router.post("/upload/{product_id}")
async def upload_data(product_id:str,
                      file:UploadFile,
                      app_settings:Settings=Depends(get_settings)):
    data_controller=DataController()
    # validate file type and size
    is_valid , signal =data_controller.validate_upload_file(file)
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                           content={"signal": signal})
    
    project_dir_path=ProjectController().get_project_path(product_id)
    file_path=data_controller.generate_unique_file_name(file.filename,
                                                         product_id)
    
    try : 
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await out_file.write(chunk)
    except Exception as e:
        logger.error(f"Error occurred while uploading file: {str(e)}")

        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"signal": ResponseSignal.FILE_UPLOAD_FAILED.value,
                                     "error": str(e)})
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value})