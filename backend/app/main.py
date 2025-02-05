from fastapi import FastAPI
from app.routers import energy

app = FastAPI()

# Include your router
app.include_router(energy.router)
