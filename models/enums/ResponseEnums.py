from enum import Enum 

class ResponseSignal(Enum):
    FILE_VALIDATE_SUCCESS = "File validated successfully"
    FILE_SIZE_EXCEEDS = "File size exceeds the limit"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_UPLOAD_FAILED = "File upload failed"