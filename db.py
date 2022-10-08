from tinydb import TinyDB

db = TinyDB('./db.json') # create a db for storing all verse

def insert(id, chapter, verse, description, author_name):
  db.insert({
    'id': id,
    'chapter': chapter,
    'verse': verse,
    'description': description,
    'author_name': author_name
  })
