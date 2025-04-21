import unittest
import numpy as np
from knowledge_distiller.qkd_distiller import QKDDistiller
from knowledge_distiller.teacher_model import TeacherModel
from knowledge_distiller.student_model import StudentModel
from knowledge_distiller.aqkd_utils import preprocess_data, split_data

class TestQKDDistiller(unittest.TestCase):
    def setUp(self):
        """Set up the QKD distiller for testing."""
        self.teacher_model = TeacherModel(n_qubits=3)
        self.student_model = StudentModel(n_qubits=3)
        self.distiller = QKDDistiller(self.teacher_model, self.student_model)

    def test_distill_knowledge(self):
        """Test the knowledge distillation process."""
        data = np.random.rand(100, 3)
        labels = np.random.randint(0, 2, size=100)  # Simulated labels for training
        self.teacher_model.train(data, labels)  # Train the teacher model first
        self.distiller.distill_knowledge(data, epochs=10)
        
        # Check if the student model has been trained (placeholder logic)
        # Here we can check if the model's parameters have changed or if it can make predictions
        test_data = np.random.rand(20, 3)
        predictions = self.student_model.predict(test_data)
        self.assertEqual(predictions.shape[0], test_data.shape[0])

    def test_evaluate_student(self):
        """Test evaluation of the student model."""
        test_data = np.random.rand(20, 3)
        test_labels = np.random.randint(0, 2, size=20)  # Simulated labels for testing
        accuracy = self.distiller.evaluate_student(test_data, test_labels)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

class TestTeacherModel(unittest.TestCase):
    def setUp(self):
        """Set up the Teacher model for testing."""
        self.teacher_model = TeacherModel(n_qubits=3)

    def test_predict(self):
        """Test the prediction capability of the teacher model."""
        data = np.random.rand(10, 3)  # 10 samples
        predictions = self.teacher_model.predict(data)
        self.assertEqual(predictions.shape[0], data.shape[0])

class TestStudentModel(unittest.TestCase):
    def setUp(self):
        """Set up the Student model for testing."""
        self.student_model = StudentModel(n_qubits=3)

    def test_train_and_predict(self):
        """Test training and prediction of the student model."""
        data = np.random.rand(100, 3)
        teacher_predictions = np.random.randint(0, 2, size=100)  # Simulated teacher predictions
        self.student_model.train(data, teacher_predictions)

        test_data = np.random.rand(20, 3)
        predictions = self.student_model.predict(test_data)
        self.assertEqual(predictions.shape[0], test_data.shape[0])

class TestAQKDUtils(unittest.TestCase):
    def test_preprocess_data(self):
        """Test data preprocessing."""
        raw_data = np.array([[1, 2], [3, 4], [5, 6]])
        processed_data = preprocess_data(raw_data)
        self.assertEqual(processed_data.shape, raw_data.shape)
        self.assertTrue(np.all(np.isfinite(processed_data)))  # Check for finite values

    def test_split_data(self):
        """Test data splitting."""
        data = np.random.rand(100, 3)
        labels = np.random.randint(0, 2, size=100)  # Simulated labels
        train_data, test_data, train_labels, test_labels = split_data(data, labels)
        self.assertEqual(train_data.shape[0] + test_data.shape[0], 100)
        self.assertEqual(train_labels.shape[0], train_data.shape[0])
        self.assertEqual(test_labels.shape[0], test_data.shape[0])

if __name__ == "__main__":
    unittest.main()
