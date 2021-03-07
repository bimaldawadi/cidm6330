import unittest
import os
from datetime import datetime
import sqlite3
import pytest

from database import DatabaseManager

from unittest.mock import Mock

class testDatabaseManager(unittest.TestCase):
    def test_execute(self):
        statement = Mock
        values = Mock
        expected = Mock
        self.assertEqual(expected, DatabaseManager._execute(statement, values))

        pytest.fixture
    def database_manager() -> DatabaseManager:
        filename = "test_bookmarks.db"
        dbm = DatabaseManager(filename)
        yield dbm
        dbm.__del__() 
        os.remove(filename)

    def test_database_manager_create_table(database_manager):
        database_manager.create_table(
        "bookmarks",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        },
    )

        conn = database_manager.connection
        cursor = conn.cursor()

        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bookmarks' ''')

        assert cursor.fetchone()[0] == 1
    
        database_manager.drop_table("bookmarks")

    def test_database_manager_add_bookmark(database_manager):
        database_manager.create_table(
        "bookmarks",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        },
    )

    data = {
        "title": "test_title",
        "url": "http://example.com",
        "notes": "test notes",
        "date_added": datetime.utcnow().isoformat()        
    }

    # act
    database_manager.add("bookmarks", data)

    # assert
    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM bookmarks WHERE title='test_title' ''')    
    assert cursor.fetchone()[0] == 1

    def test_database_manager_delete_bookmark(database_manager):
        database_manager.create_table(
        "bookmarks",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        },
    )

    data = {
        "title": "test_title_delete",
        "url": "http://example.com",
        "notes": "test notes delete",
        "date_added": datetime.utcnow().isoformat()        
    }

   
    database_manager.add("bookmarks", data)

    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' DELETE * FROM bookmarks WHERE title='test_title_delete' ''')    
    assert cursor.fetchone()[0] == 1 


    def test_database_manager_select_bookmark(database_manager):
        database_manager.create_table(
        "bookmarks",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        },
    )

    data = {
        "title": "test_title_select",
        "url": "http://example.com",
        "notes": "test notes select",
        "date_added": datetime.utcnow().isoformat()        
    }

   
    database_manager.add("bookmarks", data)

    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM bookmarks WHERE title='test_title_select' ''')    
    assert cursor.fetchone()[0] == 1 


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
