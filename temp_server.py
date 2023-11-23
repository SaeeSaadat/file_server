from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(filename='request.log', level=logging.INFO)

@app.get("/file")
def serve_file():
    file_path = "exploit.html"
    return FileResponse(file_path)

@app.get("/flag")
def serve_flag(flag: str = Query(...)):
    logging.info("flag api has been called!!!")
    logging.info(f"flag: {flag}")
    print('FLAG: ', flag)
    

def serve_flag():
    logging.info("flag api has been called!!!")
    return "Ok"
    

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Request received: {request.method} {request.url}")
    response = await call_next(request)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)