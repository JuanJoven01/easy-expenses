from fastapi import Request, HTTPException

from dotenv import dotenv_values, load_dotenv
load_dotenv(override=False)
environment = dotenv_values(".env")

api_key = environment['API_KEY']
host = environment['HOST']

async def check_api_key(request: Request):
    provided_api_key = request.headers.get("API-KEY")
    if not provided_api_key or provided_api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return request

