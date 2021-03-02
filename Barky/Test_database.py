import unittest
from database import DatabaseManager

from unittest.mock import Mock

class testDatabaseManager(unittest.TestCase):
    def test_execute(self):
        statement = Mock
        values = Mock
        expected = Mock
        self.assertEqual(expected, DatabaseManager._execute(statement, values))

    def testcreate_table(self):
        tablename = "BookMarks"
        columns = '"Title","URL", "Notes"'
        expected = Mock
        self.assertEqual(expected, DatabaseManager.create_table(self, tablename, columns))


    def testadd(self):
        tablename = "BookMarks"
        data = Mock
        expected = Mock
        self.assertEqual(expected, DatabaseManager.add(self, tablename,data))

    def testdeletee(self):
        tablename = "BookMarks"
        criteria =  Mock
        expected = Mock
        self.assertEqual(expected, DatabaseManager.delete(self, tablename, criteria))

    def testselect(self):
        tablename = "BookMarks"
        criteria = Mock
        orderby = "title"
        expected = Mock
        self.assertEqual(expected, DatabaseManager.select(self, tablename, criteria, orderby))
