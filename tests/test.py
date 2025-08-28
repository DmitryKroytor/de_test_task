from datetime import datetime
import pandas as pd
from fastapi.testclient import TestClient
from service.main import app
from models.data_model import DataModelDto
from service.global_constants import TEST_CSV_PATH

client = TestClient(app)

def test_predict():
    df: pd.DataFrame = pd.read_csv(TEST_CSV_PATH)
    dto_list: list[DataModelDto] = []
    for _, row in df.iterrows():
        row_dict = row.to_dict()
        if isinstance(row_dict.get("time_check"), str):
            row_dict["time_check"] = datetime.fromisoformat(row_dict["time_check"])
        dto_list.append(DataModelDto(**row_dict))

    dto_dicts = [dto.model_dump() for dto in dto_list]
    for dto in dto_dicts:
        dto["time_check"] = dto["time_check"].isoformat()

    resp = client.post("/predict", json=dto_dicts)

    assert resp.status_code == 200
    assert len(resp.json()) == len(dto_list)