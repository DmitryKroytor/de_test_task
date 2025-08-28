import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "micromodel.cbm")
TEST_CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test_data.csv")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
if not os.path.exists(TEST_CSV_PATH):
    raise FileNotFoundError(f"Test data file not found: {TEST_CSV_PATH}")