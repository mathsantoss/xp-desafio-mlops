#src/xp_mlops/app.py
from src.xp_mlops.create_app import create_app
import uvicorn

"""
  Entry point to FastAPI
"""

application = create_app()  # Cria a aplicação

if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000, reload=True)  # Use uvicorn para rodar a app
