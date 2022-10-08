from api_request import get_translations
import db
from normalize import normal

# There are 18 chapters in the Bhagavad geeta and 701 verses in total. These are cnt of verse of each chapter
geeta = [47, 72, 43, 42, 29, 47, 30, 28, 34, 42, 55, 20, 35, 27, 20, 24, 28, 78]

id_cnt = 1

for chapter in range(0, 18):
  chapter_num = chapter + 1
  verse_cnt = geeta[chapter]

  for verse in range(1, verse_cnt + 1):
    translations = get_translations(chapter_num, verse)
    for x in translations:
      if x["language"] == "english" and x["author_name"] == "Swami Adidevananda":
        id = id_cnt
        desc = normal(x["description"])
        author = x["author_name"]
        db.insert(id, chapter_num, verse, desc, author)
        id_cnt += 1