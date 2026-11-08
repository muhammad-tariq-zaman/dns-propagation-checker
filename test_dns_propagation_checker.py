import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

def row(res, rec, val):
    return {"resolver": res, "record": rec, "value": val}

class TestPropagation(unittest.TestCase):
    def test_consistent(self):
        self.assertEqual(check([row("8.8.8.8", "www.example.com", "1.2.3.4"), row("1.1.1.1", "www.example.com", "1.2.3.4")])[0][1], "CONSISTENT")
    def test_differs(self):
        r = check([row("8.8.8.8", "www.example.com", "1.2.3.4"), row("1.1.1.1", "www.example.com", "5.6.7.8")])
        self.assertEqual(r[0][1], "DIFFERS")
        self.assertEqual(r[0][3], ["1.1.1.1"])
    def test_single_resolver_consistent(self):
        self.assertEqual(check([row("8.8.8.8", "www.example.com", "1.2.3.4")])[0][1], "CONSISTENT")
    def test_differs_first(self):
        r = check([row("A", "a.example", "1.1.1.1"), row("B", "a.example", "1.1.1.1"), row("A", "b.example", "1.1.1.1"), row("B", "b.example", "2.2.2.2")])
        self.assertEqual(r[0][0], "b.example")
