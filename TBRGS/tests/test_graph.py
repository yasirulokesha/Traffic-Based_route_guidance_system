import unittest
from TBRGS.src.graph import SCATSNode, RoadGraph

class TestSCATSGraph(unittest.TestCase):
    def test_node_creation(self):
        node = SCATSNode(101, "Main St", "High St", -37.81, 145.05)
        self.assertEqual(node.id, 101)
        self.assertEqual(node.road_1, "Main St")
        self.assertEqual(node.road_2, "High St")
        self.assertEqual(node.latitude, -37.81)
        self.assertEqual(node.longitude, 145.05)
        self.assertEqual(len(node.neighbors), 0)
        print("✅ Node creation test passed.")

    def test_distance_calculation(self):
        node1 = SCATSNode(101, "A", "B", -37.81, 145.05)
        node2 = SCATSNode(102, "C", "D", -37.82, 145.06)
        distance = node1.distance_to(node2)
        self.assertGreater(distance, 0)
        self.assertAlmostEqual(distance, 1.4, delta=0.5)  # Within ~0.5km
        print("✅ Distance calculation test passed.")

    def test_add_node_to_graph(self):
        graph = RoadGraph()
        node = SCATSNode(101, "Main", "Cross", -37.8, 145.0)
        graph.add_node(node)
        self.assertIn(101, graph.nodes)
        print("✅ Add node to graph test passed.")

    def test_prevent_duplicate_nodes(self):
        graph = RoadGraph()
        node1 = SCATSNode(101, "X", "Y", -37.8, 145.0)
        node2 = SCATSNode(101, "X", "Y", -37.8, 145.0)
        graph.add_node(node1)
        graph.add_node(node2)  # Should be ignored
        self.assertEqual(len(graph.nodes), 1)
        print("✅ Prevent duplicate nodes test passed.")

    def test_add_edge_and_neighbors(self):
        graph = RoadGraph()
        node1 = SCATSNode(101, "A", "B", -37.8, 145.0)
        node2 = SCATSNode(102, "C", "D", -37.81, 145.01)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_edge(101, 102, 5.0)
        self.assertIn((102, 5.0), graph.edges[101])
        self.assertIn(102, node1.neighbors)
        print("✅ Add edge and neighbors test passed.")

    def test_max_neighbors_limit(self):
        node = SCATSNode(101, "A", "B", -37.8, 145.0)
        for i in range(5):
            node.add_neighbor(i)
        self.assertEqual(len(node.neighbors), 5)
        node.add_neighbor(999)  # Should not be added
        self.assertEqual(len(node.neighbors), 5)
        print("✅ Max neighbors limit test passed.")
        
    def test_remove_all_edges(self):
        graph = RoadGraph()
        n1 = SCATSNode(1, "A", "B", -37.8, 145.0)
        n2 = SCATSNode(2, "C", "D", -37.81, 145.01)
        graph.add_node(n1)
        graph.add_node(n2)
        graph.add_edge(1, 2, 10.0)
        graph.remove_all_edges()
        self.assertEqual(len(graph.edges), 0)
        self.assertEqual(len(n1.neighbors), 0)
        print("✅ Remove all edges test passed.")

# if __name__ == '__main__':
#     unittest.main()
