from pathlib import Path
import logging
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from src.views import view
from src.utils import logger


def create_app(config_path: Path = Path("configs/logging_config.json")) -> FastAPI:
    logger.CustomizeLogger.make_logger(config_path)

    app = FastAPI(
        title="YouTube statistic",
        debug=False,
        docs_url='/api/swagger',
        redoc_url='/api/reswag',
        openapi_url='/api/openapi.json'),
    app.logger = logger
    app.secret_key = os.getenv("SECRET_KEY")

    @app.exception_handler(Exception)
    async def unicorn_exception_handler(request: Request, exc: Exception):
        logging.error(exc)
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logging.error(exc)
        return JSONResponse(
            status_code=422,
            content={"message": str(exc)},
        )

    app.include_router(
        view.router,
        prefix="/api/v1",
        tags=["view"],
    )
    return app
