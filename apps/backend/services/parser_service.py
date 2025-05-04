import hcl2
from fastapi import UploadFile, HTTPException
from typing import Dict, Any
from apps.backend.models.terraform_schema import Provider, Resource, TerraformSchema

async def parse_tf_file(file: UploadFile):
    if not file.filename.endswith(".tf"):
        raise HTTPException(status_code=400, detail="Not a .tf file")

    content = await file.read()
    parsed = hcl2.loads(content.decode())
    return parsed


def transform_to_schema(parsed: dict) -> dict:
    providers = []
    resources = []

    if "provider" in parsed:
        for provider_block in parsed["provider"]:
            for provider_name, provider_config in provider_block.items():
                providers.append(Provider(name=provider_name, config=provider_config))

    if "resource" in parsed:
        for resource_block in parsed["resource"]:
            for resource_type, resource_instances in resource_block.items():
                for resource_name, resource_config in resource_instances.items():
                    resources.append(Resource(type=resource_type, name=resource_name, config=resource_config))

    schema = TerraformSchema(providers=providers, resources=resources)

    return schema.model_dump()
