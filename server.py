from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

app = FastAPI()

from modules.health.route import *
from modules.version.route import *
from modules.entry.route import *


@app.exception_handler(RequestValidationError)
async def error_422_to_400(request: Request, exc):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": exc.errors()}),
    )
