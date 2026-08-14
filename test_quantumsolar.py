# test_quantumsolar.py
"""
Tests for QuantumSolar module.
"""

import unittest
from quantumsolar import QuantumSolar

class TestQuantumSolar(unittest.TestCase):
    """Test cases for QuantumSolar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumSolar()
        self.assertIsInstance(instance, QuantumSolar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumSolar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
