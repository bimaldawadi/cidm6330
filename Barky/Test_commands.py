import unittest

from unittest.mock import Mock

from database import DatabaseManager

from commands import CreateBookmarksTableCommand, AddBookmarkCommand, ListBookmarksCommand, DeleteBookmarkCommand, ImportGitHubStarsCommand, EditBookmarkCommand

class testCreateBookmarksTableCommand(unittest.TestCase):

    def test_execute(self):
        db = DatabaseManager("bookmarks.db")
        mockDb = Mock
        self.assertEqual(db.create_table, mockDb)


class testAddBookmarkCommand(unittest.TestCase):
    def test_execute(self):
        expected = "Bookmark added!"
        data = Mock
        timestamp = Mock
        self.assertEqual(expected, AddBookmarkCommand.execute(self, data, timestamp))

class testListBookmarksCommand(unittest.TestCase):
    def test_execute(self):
        db = Mock
        self.assertEqual(db, ListBookmarksCommand.execute(self))

class testDeleteBookmarkCommand(unittest.TestCase):
    def test_execute(self):
        data = Mock
        expected = "Bookmark deleted!"
        self.assertEqual(expected, DeleteBookmarkCommand.execute(self,data))

class testImportGitHubStarsCommand(unittest.TestCase):
    def test_esecute(self):
        expected = "Imported 0 bookmarks from starred repos!"
        data = Mock
        self.assertEqual(expected, ImportGitHubStarsCommand.execute(self, data))

class testEditBookmarkCommand(unittest.TestCase):
    def test_execute(self):
        expected = "Bookmark updated!"
        data = Mock
        self.assertEqual(expected, EditBookmarkCommand.execute(self,data))