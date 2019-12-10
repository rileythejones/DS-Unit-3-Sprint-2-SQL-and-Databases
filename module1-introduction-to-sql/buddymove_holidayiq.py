import pandas as pd
import sqlite3

df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('reviews', con=conn)


def sql_answer(question, query):
    curs = conn.cursor()
    output = curs.execute(query).fetchall()
    curs.close()
    conn.commit()
    return print(question, output)


sql_answer("Count how many rows you have - it should be 249!",
 """SELECT COUNT(*) from reviews;""")

sql_answer("""How many users who reviewed at least 100 Nature in the category
 also reviewed at least 100 in the Shopping category?""", """SELECT COUNT(*)
  FROM reviews WHERE Nature > 100 AND Shopping > 100;""")

sql_answer("""What are the average number of reviews for each category?""",
"""SELECT
(SELECT AVG(Nature) FROM reviews) as av_nature,
(SELECT AVG(Sports) FROM reviews) as av_sports,
(SELECT AVG(Theatre) FROM reviews) as av_theatre,
(SELECT AVG(Shopping) FROM reviews) as av_shopping,
(SELECT AVG(Picnic) FROM reviews) as av_picnic,
(SELECT AVG(Religious) FROM reviews) as av_relgious;""")