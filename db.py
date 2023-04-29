from tinydb import TinyDB, Query

db = TinyDB("./db.json")  # create a db for storing all verse
entry = Query()


def insert(id, chapter, verse, description, author_name):
    db.insert(
        {
            "id": id,
            "chapter": chapter,
            "verse": verse,
            "description": description,
            "author_name": author_name,
        }
    )


def get_description(id):
    return db.search(entry.id == id)[0]["description"]
