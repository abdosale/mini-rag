from controllers.BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
import os
import  re
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
    def generate_unique_file_name(self,original_file_name:str,project_id:str):
        random_key=self.generate_random_string(10)
        project_path=ProjectController().get_project_path(project_id)
        cleaned_file_name=self.clean_file_name(original_file_name)
        new_file_path=os.path.join(project_path,
                                   random_key+"_"+\
                                    cleaned_file_name)

        while os.path.exists(new_file_path):
            random_key=self.generate_random_string(10)
            new_file_path=os.path.join(project_path,
                                   random_key+"_"+\
                                    cleaned_file_name)

        return new_file_path

    def clean_file_name(self,original_file_name:str):
        cleaned_name = re.sub(r'[^\w.]','', original_file_name.strip())
        cleaned_name =  original_file_name.replace(" ","_").lower()
        return cleaned_name
