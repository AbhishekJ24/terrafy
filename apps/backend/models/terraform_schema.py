from pydantic import BaseModel
from typing import Dict, Any, List

class Provider(BaseModel):
    name: str
    config: Dict[str, Any]

class Resource(BaseModel):
    type: str
    name: str
    config: Dict[str, Any]

class TerraformSchema(BaseModel):
    providers: List[Provider] = []
    resources: List[Resource] = []
