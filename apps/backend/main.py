from fastapi import FastAPI
from apps.backend.api.visualize import router

app = FastAPI()
app.include_router(router)
