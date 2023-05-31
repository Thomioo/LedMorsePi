from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from morse import Say
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def func():
    return FileResponse(path="./ui/index.html", status_code=200)

@app.get("/script.js")
def f():
    return FileResponse(path="./ui/script.js", status_code=200)

@app.get("/style.css")
def f():
    return FileResponse(path="./ui/style.css", status_code=200)

@app.get("/say")
def f(s):
    Say(s)
    return "sent: " + s
        # send requests in format ?s=<the text you want here>
if __name__ == "__main__":
#       uvicorn.run(app, host="192.168.2.241", port=8000, log_level="error")
#       uvicorn.run(app, host="192.168.2.241", port=8000)
        uvicorn.run(app, host="localhost", port=8000)