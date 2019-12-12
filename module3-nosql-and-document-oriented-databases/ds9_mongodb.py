import pymongo

client = pymongo.MongoClient("mongodb+srv://rileymjones:D8x-#.u8_pi4TPA@cluster0-xcg95.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


db.test.insert_one({'x':1})


db.test.count_documents({'x':1})


db.test.find({'x':1})

curs = db.test.find({'x':1})

stephanie_doc = {
    'favorite animal': 'alpaca',
    'favorite color': 'blue'
}

zoli_michelle_doc = {
    'favorite animal': ['Black Panther', 'Unicorn']
}

dorothy_doc = {
    'favorite animal': 'dog'
}

db.test.insert_many([stephanie_doc, zoli_michelle_doc, dorothy_doc])

#LOOK AT ALL DOCUMENTS
list(db.test.find())

#make more docs
more_docs = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i 
  more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

db.test.update_one({'value':3},
                   {'$inc': {'value':5}})

list(db.test.find())

db.test.update_many({'even':True},
                    {'$inc': {'value':100}})

list(db.test.find())

db.test.delete_many({'even':False})

list(db.test.find())

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)
#you would get error if you did db.test.insert_one(rpg_character)

#here is how to cast to dictionary
db.test.insert_one({'rpg_character': rpg_character})

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

list(db.test.find())

