import hcl2
from fastapi import UploadFile, HTTPException

async def parse_tf_file(file: UploadFile):
    if not file.filename.endswith(".tf"):
        raise HTTPException(status_code=400, detail="Not a .tf file")

    content = await file.read()
    parsed = hcl2.loads(content.decode())
    return parsed
