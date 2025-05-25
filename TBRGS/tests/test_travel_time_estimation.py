import unittest
from unittest.mock import patch
from ..src.graph import SCATSNode, RoadGraph
from ..src.travel_time_estimator import calculate_travel_time  # Adjust this import based on where your function is

class TestTravelTime(unittest.TestCase):
    
    def setUp(self):
        # Create a mock graph with two nodes
        self.graph = RoadGraph()
        self.node1 = SCATSNode(101, "Main", "1st", -37.81, 145.05)
        self.node2 = SCATSNode(102, "Main", "2nd", -37.82, 145.06)
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.timestamp = "2006-11-01 00:00"

    @patch('models.LSTM_model.LSTM_prediction', return_value=400)
    def test_lstm_travel_time(self, mock_lstm):
        result = calculate_travel_time(self.graph, 101, 102, self.timestamp, model="lstm")
        self.assertIsNotNone(result)
        self.assertTrue(float(result) > 0)
        print(f"✅ LSTM test passed with travel time: {result} minutes")

    @patch('models.GRU_model.GRU_prediction', return_value=400)
    def test_gru_travel_time(self, mock_gru):
        result = calculate_travel_time(self.graph, 101, 102, self.timestamp, model="gru")
        self.assertIsNotNone(result)
        self.assertTrue(float(result) > 0)
        print(f"✅ GRU test passed with travel time: {result} minutes")

    @patch('models.RNN_model.RNN_prediction', return_value=400)
    def test_rnn_travel_time(self, mock_rnn):
        result = calculate_travel_time(self.graph, 101, 102, self.timestamp, model="rnn")
        self.assertIsNotNone(result)
        self.assertTrue(float(result) > 0)
        print(f"✅ RNN test passed with travel time: {result} minutes")

    def test_invalid_model(self):
        result = calculate_travel_time(self.graph, 101, 102, self.timestamp, model="invalid")
        self.assertIsNone(result)
        print(f"✅ Invalid model test passed.")

    @patch('models.LSTM_model.LSTM_prediction', return_value=None)
    def test_missing_flow_data(self, mock_lstm):
        result = calculate_travel_time(self.graph, 101, 102, self.timestamp, model="lstm")
        self.assertIsNone(result)
        print(f"✅ Missing flow data test passed.")

# if __name__ == "__main__":
#     unittest.main()
