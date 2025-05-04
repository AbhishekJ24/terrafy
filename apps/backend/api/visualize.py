from fastapi import APIRouter, File, UploadFile, HTTPException
from apps.backend.services.visualize_service import handle_visualization

router = APIRouter()

@router.post("/visualize")
async def visualize(file: UploadFile = File(...)):
    if not file.filename.endswith((".tf", ".tfstate", ".tfplan")):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    
    result = await handle_visualization(file)
    return result
