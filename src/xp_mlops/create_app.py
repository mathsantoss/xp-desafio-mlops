import os

from fastapi import FastAPI
from _version import __version__
from src.xp_mlops.api.http.health import router as health_router
from src.xp_mlops.api.http.predict import router as predict_router


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app() -> FastAPI:
    """Creates app in function with the FastAPI framework.

    :return: FastAPI App
    """

    app = FastAPI(
        title="MLOPS API",
        version=__version__,
        sumary="API is resposible to make real time inference.",
        description="XP",
        docs_url="/docs",
        redoc_url="/redoc",
        contact={"name": "XP MLOPS Team"},
    )

    app.include_router(health_router)
    app.include_router(predict_router, prefix="/api")

    return app
