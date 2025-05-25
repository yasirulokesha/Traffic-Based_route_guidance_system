import unittest
import numpy as np
from .test_graph import TestSCATSGraph
from TBRGS.src.models.LSTM_model import LSTM_prediction
from TBRGS.src.models.GRU_model import GRU_prediction
from TBRGS.src.models.RNN_model import RNN_prediction

from TBRGS.src.travel_time_estimator import calculate_travel_time
from TBRGS.src.data_processing import process_scats_data


class TestLSTMModel(unittest.TestCase):
    def test_lstm_prediction_output(self):
        site_id = "970"  # Example valid SCATS site ID
        timestamp = "2006-11-01 00:00"  # Example timestamp
        prediction = LSTM_prediction(site_id, timestamp)
        self.assertIsInstance(prediction, float, "❌ LSTM prediction is not a float32")
        print("✅ UT-08: LSTM prediction in [0, 1] passed.")

class TestGRUModel(unittest.TestCase):
    def test_gru_prediction_output(self):
        site_id = "970"  # Example valid SCATS site ID
        timestamp = "2006-11-01 00:00"  # Example timestamp
        prediction = GRU_prediction(site_id, timestamp)
        self.assertIsInstance(prediction, float, "❌ GRU prediction is not a float32")
        print("✅ UT-09: GRU prediction in [0, 1] passed.")
        
class TestRNNModel(unittest.TestCase):
    def test_rnn_prediction_output(self):
        site_id = "970"  # Example valid SCATS site ID
        timestamp = "2006-11-01 00:00"  # Example timestamp
        prediction = RNN_prediction(site_id, timestamp)
        self.assertIsInstance(prediction, float, "❌ RNN prediction is not a float32")
        print("✅ UT-10: RNN prediction in [0, 1] passed.")
        
class TestTimeEstimate(unittest.TestCase):
    def test_travel_time_estimation(self):
        
        graph = process_scats_data()
        origin_id = "970"  # Example valid SCATS site ID
        destination_id = "3685"  # Example valid SCATS site ID
        timestamp = "2006-11-01 00:00"  # Example timestamp
        
        travel_time = calculate_travel_time(graph, origin_id, destination_id, timestamp, model="lstm")
        self.assertIsNotNone(travel_time, "❌ Travel time estimation returned None")
        self.assertTrue(float(travel_time) > 0, "❌ Travel time must be positive")
        print(f"✅ UT-11: Travel time estimation passed with {travel_time} minutes.")

if __name__ == "__main__":
    unittest.main(verbosity=0)  # Run all tests in the TestSCATSGraph class