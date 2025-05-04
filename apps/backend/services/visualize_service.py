from fastapi import UploadFile
from apps.backend.services.parser_service import parse_tf_file, transform_to_schema
from apps.backend.models.responses import SuccessResponse

async def handle_visualization(file: UploadFile):
    parsed_data = await parse_tf_file(file)
    transformed_data = transform_to_schema(parsed_data)
    data = {
        "filename": file.filename,
        "parsed": parsed_data,
        "transformed": transformed_data
    }
    return SuccessResponse(data=data)

