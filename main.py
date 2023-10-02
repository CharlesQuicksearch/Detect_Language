import json

from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from detect_language import detect_language
from Config_Logger import logger
from Config_Logger.logger import logging
import schedule
import uvicorn

app = FastAPI()

logging.info("Application running")

logger.config_logger()

#Start writing logs in a new logging file
schedule.every().day.at("00:00").do(logger.config_logger)

@app.get("/home")
def home():
    return "Detect language API. Call /detect_language/"

@app.post("/detect_language/", response_model=Response)
async def detect(request_data: Request):
    logging.info(f"Request: {request_data.input}")
    try:
        language_result = await detect_language(request_data.input)
        logging.info(f"200 {language_result}")
        return Response(output=language_result)

    except Exception as e:
        logging.warning(f"500 {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
    uvicorn.run(app, host=config.get("host"), port=int(config.get("port")))
