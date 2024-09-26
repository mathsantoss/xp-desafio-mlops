"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.wine_pipeline import create_pipeline as create_wine_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    # Adicionar o pipeline de vinho
    pipelines["wine_pipeline"] = create_wine_pipeline()
    
    # Criar um pipeline padrão que soma todos os pipelines registrados
    if pipelines:
        pipelines["__default__"] = sum(pipelines.values())
    else:
        raise ValueError("Nenhum pipeline encontrado")
    return pipelines
