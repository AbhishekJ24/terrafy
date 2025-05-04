import os
import shutil
from fastapi import UploadFile
from uuid import uuid4

def save_upload_file(file: UploadFile, destination_dir: str) -> str:
    os.makedirs(destination_dir, exist_ok=True)

    unique_filename = f"{uuid4()}_{file.filename}"
    file_path = os.path.join(destination_dir, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
