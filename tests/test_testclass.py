from os.path import (join, abspath, dirname)
import unittest
from testclass.testclass import TestClass


class TestTestClass(unittest.TestCase):
    def test_load_testclass(self):
        test_send = """{
  allFood {
    edges {
      node {
        description
        id
        fdcId
        dataType
        foodCategoryId
        publicationDate
      }
    }
  }
}
"""
        test_request = {'data': {'allFood': {'edges': [
            {'node': {
                'description': 'WOLF Chili Without Beans',
                'id': 'Rm9vZDozNDY0NjQ=', 'fdcId': '346464',
                'dataType': 'branded_food', 'foodCategoryId': 0,
                'publicationDate': '2019-04-01 00:00:00'}},
            {'node': {
                'description': 'SANALAC Non Fat Dry Milk, 1 QT',
                'id': 'Rm9vZDozNDY0NzA=', 'fdcId': '346470',
                'dataType': 'branded_food', 'foodCategoryId': 0,
                'publicationDate': '2019-04-01 00:00:00'}},
            {'node': {
                'description': 'SWISS MISS Hot Cocoa Mix Dark Chocolate'
                               ' Sensation Envelopes, 10 OZ',
                'id': 'Rm9vZDozNDY1MTk=', 'fdcId': '346519',
                'dataType': 'branded_food', 'foodCategoryId': 0,
                'publicationDate': '2019-04-01 00:00:00'}},
            {'node': {
                'description': 'SWISS MISS Creamy Vanilla Pudding, 24 OZ',
                'id': 'Rm9vZDozNDY1MzI=', 'fdcId': '346532',
                'dataType': 'branded_food', 'foodCategoryId': 0,
                'publicationDate': '2019-04-01 00:00:00'}},
            {'node': {
                'description': 'SWISS MISS Creamy Milk Chocolate Pudding'
                               ', 24 OZ"',
                'id': 'Rm9vZDozNDY1MzM=', 'fdcId': '346533',
                'dataType': 'branded_food', 'foodCategoryId': 0,
                'publicationDate': '2019-04-01 00:00:00'
            }}]}}}
        dir_name = join(abspath(dirname(__file__)), 'files')
        test_name = 'test_one'
        test = TestClass(dir_name, test_name)
        test.load_files()
        self.assertEqual(dir_name, test._dir_name,
                         "Directory name doesn't match")
        self.assertEqual(test_name, test._test_name,
                         "Test name doesn't match")
        self.assertEqual(test_request, test._expected_result,
                         "Expected results doesn't match")
        self.assertEqual(test_send, test._send_request,
                         "Send request doesn't match")


if __name__ == '__main__':
    unittest.main()
