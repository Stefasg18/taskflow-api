from fastapi import FastAPI
from app.routers import auth, tasks

app = FastAPI(title="TaskFlow API", version="1.0.0")
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
