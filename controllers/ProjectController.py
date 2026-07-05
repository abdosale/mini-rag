from .BaseController import BaseController
from fastapi import UploadFile
from models.enums import ResponseSignal
import os


class ProjectController(BaseController):
    def __init__(self):
        super().__init__()


    def get_project_path(self,project_id:str):
        project_path=os.path.join(self.file_dir,project_id)

        if not os.path.exists(project_path):
            os.mkdir(project_path)
        return project_path