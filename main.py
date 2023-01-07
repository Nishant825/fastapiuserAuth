import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
# from routes.api import router as api_router

from auth.routes import app

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)
    print("running")
