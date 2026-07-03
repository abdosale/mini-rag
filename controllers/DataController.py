from controllers.BaseController import BaseController
from fastapi import UploadFile
from models.enums import ResponseSignal
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1024*1024
    def validate_upload_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size>self.app_settings.FILE_MAX_SIZE*self.size_scale:
            return False,ResponseSignal.FILE_SIZE_EXCEEDS.value
        return True ,ResponseSignal.FILE_UPLOAD_SUCCESS.value