from fastapi import UploadFile
from apps.backend.utils.file_utils import save_upload_file
from apps.backend.services.parser import parse_tf_file

async def handle_visualization(file: UploadFile):
    # Save the uploaded file locally (optional in prod)
    UPLOAD_DIR = "apps/backend/uploaded_files"
    file_path = save_upload_file(file, UPLOAD_DIR)

    # Parse the Terraform file
    parsed_data = await parse_tf_file(file)

    return {
        "filename": file.filename,
        "path": file_path,
        "parsed": parsed_data,
    }
