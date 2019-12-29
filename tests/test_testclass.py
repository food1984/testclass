from os.path import (join, abspath, dirname)
import unittest
from testclass.testclass import TestClass


class TestTestClass(unittest.TestCase):
    def test_load_testclass(self):
        dir_name = join(abspath(dirname(__file__)), 'files')
        test_name = 'test_one'
        test = TestClass(dir_name, test_name)
        test.load_files()
        self.assertEqual(dir_name, test._dir_name)
        self.assertEqual(test_name, test._test_name)


if __name__ == '__main__':
    unittest.main()
