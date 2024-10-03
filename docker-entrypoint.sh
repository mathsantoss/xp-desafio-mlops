#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Rodar o Kedro para compilar e preparar o pipeline
kedro run

# Iniciar o FastAPI com Uvicorn
exec uvicorn src.xp_mlops.app:aplication --host 0.0.0.0 --port 8000
