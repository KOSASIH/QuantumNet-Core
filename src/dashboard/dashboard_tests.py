# src/dashboard/dashboard_tests.py

import unittest
from fastapi.testclient import TestClient
from backend.api import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.api import MetricModel, Base

# Database setup for testing
DATABASE_URL = "sqlite:///./test_metrics.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create the database tables
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        # Drop the database tables
        Base.metadata.drop_all(bind=engine)

    def setUp(self):
        self.client = TestClient(app)
        self.db = TestingSessionLocal()

    def tearDown(self):
        self.db.close()

    def test_add_metric(self):
        response = self.client.post("/api/v1/metrics/", json={"name": "test_metric", "value": 42.0})
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())  # Check if ID is returned
        self.assertEqual(response.json()["name"], "test_metric")
        self.assertEqual(response.json()["value"], 42.0)

    def test_get_metrics(self):
        self.client.post("/api/v1/metrics/", json={"name": "test_metric", "value": 42.0})
        response = self.client.get("/api/v1/metrics/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

    def test_add_metric_invalid(self):
        response = self.client.post("/api/v1/metrics/", json={"name": "", "value": 42.0})  # Invalid name
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_aggregate_metrics(self):
        self.client.post("/api/v1/metrics/", json={"name": "metric1", "value": 10.0})
        self.client.post("/api/v1/metrics/", json={"name": "metric2", "value": 20.0})
        self.client.post("/api/v1/metrics/", json={"name": "metric3", "value": 30.0})

        response = self.client.get("/api/v1/metrics/aggregate/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["average"], 20.0)
        self.assertEqual(response.json()["min"], 10.0)
        self.assertEqual(response.json()["max"], 30.0)

    def test_get_metrics_empty(self):
        response = self.client.get("/api/v1/metrics/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])  # Should return an empty list

if __name__ == "__main__":
    unittest.main()
