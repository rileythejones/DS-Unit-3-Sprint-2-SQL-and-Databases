import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')


def sql_answer(question, query):
    curs = conn.cursor()
    output = curs.execute(query).fetchall()
    curs.close()
    conn.commit()
    return print(question, output)


sql_answer("How many total Characters are there?",
 """SELECT COUNT(*) FROM charactercreator_character;""")

sql_answer("How many of each specific subclass?",
 """SELECT
(SELECT COUNT(*) FROM charactercreator_cleric) as cleric,
(SELECT COUNT(*) FROM charactercreator_fighter) as fighter, 
(SELECT COUNT(*) FROM charactercreator_mage) as mage,
(SELECT COUNT(*) FROM charactercreator_necromancer) as necromancer,
(SELECT COUNT(*) FROM charactercreator_thief) as thief;""")

sql_answer("How many total Items?",
 """SELECT COUNT(*) FROM charactercreator_character_inventory;""")

sql_answer("How many of the Items are weapons?",
 """SELECT COUNT(*) FROM armory_weapon
INNER JOIN charactercreator_character_inventory ON
item_id = item_ptr_id;""")

sql_answer("How many are not?",
 """SELECT
	(SELECT COUNT(*) FROM charactercreator_character_inventory)
	-(SELECT COUNT(*) FROM armory_weapon
INNER JOIN charactercreator_character_inventory ON
item_id = item_ptr_id)""")

sql_answer("How many Items does each character have? (Return first 20 rows)",
 """SELECT character_id, COUNT(*)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;""")


sql_answer("""How many Weapons does each character have? (Return first 20 rows)

(note: this list only lists character ids that have weapons, so it isn't listed in means that character has zero weapons.)
""",
 """SELECT character_id, COUNT(*) FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON item_id = item_ptr_id
GROUP BY character_id
LIMIT 20;""")

sql_answer("On average, how many Items does each Character have?",
 """SELECT avg(count)
	FROM
	(
SELECT character_id, COUNT(*) as count
FROM charactercreator_character_inventory
GROUP BY character_id
)""")

sql_answer("""On average, how many Weapons does each character have?

(note this lists the average number of weapons that weapon having characters have)
""",
 """SELECT avg(count)
	FROM
	(
SELECT character_id, COUNT(*) as count FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON item_id = item_ptr_id
GROUP BY character_id)""")


