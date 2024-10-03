import numpy as np
import joblib
from datetime import datetime
from src.xp_mlops.model.dataclass.v1.inference_response import InferenceResponse
from src.xp_mlops.model.dataclass.v1.features_input import FeaturesInput
from fastapi import APIRouter


model = joblib.load("src/model/model.pkl")


router = APIRouter()


@router.post(
    "/predict",
    tags=["xp-mlops"],
    summary="Predict model",
    description="This endpoint is used to make inference requests",
    response_description="inference handler",
    response_model=InferenceResponse,
)
async def predict(payload: FeaturesInput):
    started_at = datetime.now().isoformat()

    # Transformar as features em um formato apropriado para o modelo
    input_data = np.array(
        [
            payload.malic_acid,
            payload.ash,
            payload.alcalinity_of_ash,
            payload.magnesium,
            payload.total_phenols,
            payload.flavanoids,
            payload.nonflavanoid_phenols,
            payload.proanthocyanins,
            payload.color_intensity,
            payload.hue,
            payload.od280_od315_of_diluted_wines,
            payload.proline,
        ]
    ).reshape(1, -1)

    # Realizar a previsão
    prediction = model.predict(input_data)

    finished_at = datetime.now().isoformat()
    # Retornar o resultado
    return InferenceResponse(
        result=prediction,
        started_at=started_at,
        finished_at=finished_at,
        input_features=payload,
    )
    # return {"predicted_alcohol_content": prediction[0]}
