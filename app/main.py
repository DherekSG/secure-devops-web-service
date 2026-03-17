from fastapi import FastAPI
import socket
import time

app = FastAPI()

start_time = time.time()

@app.get("/")
def home():
    return {
        "project": "Secure DevOps Web Service",
        "status": "running",
        "server": socket.gethostname()
    }

@app.get("/status")
def status():
    return {
        "service": "ok",
        "message": "Secure DevOps Lab running"
    }

@app.get("/health")
def health():
    uptime = round(time.time() - start_time, 2)

    return {
        "status": "healthy",
        "uptime_seconds": uptime,
        "service": "fastapi"
    }
