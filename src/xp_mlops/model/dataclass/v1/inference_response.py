from typing import List
from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict
from src.xp_mlops.model.dataclass.v1.features_input import FeaturesInput


class InferenceResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    started_at: datetime
    finished_at: datetime
    result: List[float]
    input_features: FeaturesInput
