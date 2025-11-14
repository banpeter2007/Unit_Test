import unittest
from age import categorize_by_age

import pytest
from age import categorize_by_age

class TestAgeCategorization(unittest.TestCase):
    def test_child_category(self):
            self.assertEqual(categorize_by_age(5), "Child")
            self.assertEqual(categorize_by_age(9), "Child")
            self.assertEqual(categorize_by_age(0), "Child")
    def test_teenager_category(self):
            self.assertEqual(categorize_by_age(10), "Teenager")
            self.assertEqual(categorize_by_age(15), "Teenager")
            self.assertEqual(categorize_by_age(18), "Teenager")
    def test_adult_category(self):
            self.assertEqual(categorize_by_age(19), "Adult")
            self.assertEqual(categorize_by_age(30), "Adult")
            self.assertEqual(categorize_by_age(64), "Adult")
    def test_golden_age_category(self):
            self.assertEqual(categorize_by_age(65), "Golden Age")
            self.assertEqual(categorize_by_age(80), "Golden Age")
            self.assertEqual(categorize_by_age(120), "Golden Age")
    def test_invalid_age(self):
            self.assertEqual(categorize_by_age(-1), "Invalid Age: -1")
            self.assertEqual(categorize_by_age(121), "Invalid Age: 121")
            self.assertEqual(categorize_by_age(150), "Invalid Age: 150")

def test_categorize_by_age_pytest():
    assert categorize_by_age(7) == "Child"
    assert categorize_by_age(16) == "Teenager"
    assert categorize_by_age(45) == "Adult"
    assert categorize_by_age(70) == "Golden Age"
    assert categorize_by_age(-5) == "Invalid Age: -5"
    assert categorize_by_age(130) == "Invalid Age: 130"

# python -m unittest .\test_age.py -v
# python -m pytest .\test_age.py -v