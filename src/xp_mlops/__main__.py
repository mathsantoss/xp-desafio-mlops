# """xp-mlops file for ensuring the package is executable
# as `xp-mlops` and `python -m xp_mlops`
# """

# from src.xp_mlops.app import create_app
# import uvicorn 
# import sys
# from pathlib import Path
# from typing import Any

# from kedro.framework.cli.utils import find_run_command
# from kedro.framework.project import configure_project


# def main(*args, **kwargs) -> Any:
#     package_name = Path(__file__).parent.name
#     configure_project(package_name)

#     interactive = hasattr(sys, 'ps1')
#     kwargs["standalone_mode"] = not interactive

#     if "--run-api" in args:  # Adicionando uma opção para rodar a API
#         app = create_app()  # Cria a aplicação FastAPI
#         uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
#     else:
#         run = find_run_command(package_name)
#         return run(*args, **kwargs)

# if __name__ == "__main__":
#     main()
