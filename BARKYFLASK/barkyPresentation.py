from flask import Flask
from dotenv import load_dotenv

from barkyService import CreateBookmarksTableCommand
from barkyService import AddBookmarkCommand
from barkyService import ListBookmarksCommand
from barkyService import DeleteBookmarkCommand
from barkyService import ImportGitHubStarsCommand
from barkyService import EditBookmarkCommand
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Barky Flask'

@app.route('/CreateBookmarksTable')
def hello_world():
    return CreateBookmarksTableCommand.execute

@app.route('/AddBookmark')
def hello_world():
    return AddBookmarkCommand.execute

@app.route('/ListBookmarks')
def hello_world():
    return ListBookmarksCommand.execute

@app.route('/DeleteBookmark')
def hello_world():
    return DeleteBookmarkCommand.execute

@app.route('/ImportGitHubStars')
def hello_world():
    return ImportGitHubStarsCommand.execute

@app.route('/EditBookmark')
def hello_world():
    return EditBookmarkCommand.execute


if __name__ == '__main__':
   app.run()