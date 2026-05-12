# test_phalanetwork.py
"""
Tests for PhalaNetwork module.
"""

import unittest
from phalanetwork import PhalaNetwork

class TestPhalaNetwork(unittest.TestCase):
    """Test cases for PhalaNetwork class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PhalaNetwork()
        self.assertIsInstance(instance, PhalaNetwork)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PhalaNetwork()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
