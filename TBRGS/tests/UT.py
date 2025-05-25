import numpy as np
import pandas as pd
from datetime import datetime

# Import relevant functions/classes
from data_processing import process_scats_data
from sequence_generator import generate_sequences
from model_predictor import predict_next_volume
from travel_time_estimator import calculate_travel_time
from route_search import find_k_shortest_routes


# UT-01: Data Preprocessing
def test_data_preprocessing():
    df = pd.read_csv("TBRGS/data/processed/scats_data.csv")
    assert not df.isnull().values.any(), "❌ Null values found in processed data"
    assert 'timestamp' in df.columns, "❌ Missing timestamp column"
    assert df['timestamp'].diff().min() >= pd.Timedelta(minutes=15), "❌ Not all data is 15-min spaced"
    print("✅ UT-01 Passed: Data Preprocessing")


# UT-02: Sequence Generator
def test_sequence_generator():
    volume_data = np.arange(200).reshape(-1, 1)  # Dummy data
    X, y = generate_sequences(volume_data, window_size=96)
    assert X.shape[1:] == (96, 1), "❌ Incorrect input shape for model"
    assert len(X) == len(y), "❌ Input and target lengths mismatch"
    print("✅ UT-02 Passed: Sequence Generator")


# UT-03: LSTM Model Prediction
def test_lstm_prediction():
    # Dummy 96-timestep input
    sample_input = np.random.rand(1, 96, 1)
    pred = predict_next_volume(site_id=970, model_type='LSTM', input_sequence=sample_input)
    assert isinstance(pred, float), "❌ Prediction is not a float"
    assert 0 <= pred <= 1, "❌ Prediction not in [0, 1] range"
    print("✅ UT-03 Passed: LSTM Model Prediction")


# UT-04: Travel Time Estimation
def test_travel_time_estimation():
    graph = process_scats_data()
    time = calculate_travel_time(graph, from_node=970, to_node=3685, timestamp="2006-11-01 00:00")
    assert isinstance(time, (float, int)), "❌ Travel time is not a number"
    assert time > 0, "❌ Travel time must be positive"
    print("✅ UT-04 Passed: Travel Time Estimation")


# UT-05: Route Search Algorithm
def test_route_search():
    graph = process_scats_data()
    paths = find_k_shortest_routes(graph, start_node=970, end_node=3804, k=5)
    assert isinstance(paths, list), "❌ Returned paths is not a list"
    assert len(paths) <= 5, "❌ More than 5 paths returned"
    for path in paths:
        assert isinstance(path[1], list), "❌ Path format incorrect"
        assert len(path[1]) >= 2, "❌ Path too short"
    print("✅ UT-05 Passed: Route Search Algorithm")


# Run all tests
if __name__ == "__main__":
    test_data_preprocessing()
    test_sequence_generator()
    test_lstm_prediction()
    test_travel_time_estimation()
    test_route_search()