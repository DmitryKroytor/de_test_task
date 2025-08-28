from catboost import CatBoostClassifier
from fastapi import FastAPI
from typing import Union
from models.data_model import DataModelDto
from service.pick_regno import pick_regno
from service.global_constants import MODEL_PATH
import logging

app = FastAPI()

model = CatBoostClassifier()
model.load_model(MODEL_PATH)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.post("/predict")
async def predict(dto: Union[DataModelDto, list[DataModelDto]]):
    try:
        logger.info(f"Prediction: received data transfer object of length {len(dto)}")
        if isinstance(dto, DataModelDto):
            dto_list = [dto]
        else:
            dto_list = dto
        results: list[list[float]] = []
        for dto in dto_list:
            logger.info(f"Processing dto: {dto}")
            attributes = dto.get_attributes()
            results.append(pick_regno(*attributes, model).tolist())
        if len(results) == 1:
            logger.info(f"Prediction completed: {results[0]}")
            return results[0]
        logger.info(f"Prediction completed: {results}")
        return results
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise e
