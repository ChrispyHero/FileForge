import unittest
from src.append import _add_newline

class TestAlgorithms(unittest.TestCase): 

    def test_add_newline(self): 
        input = ["test", "test must be equal", "FileForge!!111!", "Jesus <3"]
        result = _add_newline(input)
        control_list = ['test\n', 'test must be equal\n', 'FileForge!!111!\n', 'Jesus <3\n']
        self.assertEqual(result, control_list)

