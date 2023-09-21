from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from detect_language import detect_language

app = FastAPI()

@app.get("/")
def home():
    return "Detect language"

@app.post("/detect_language/", response_model=Response)
async def detect(request_data: Request):
    try:
        language_result = await detect_language(request_data.input)
        return Response(output=language_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
