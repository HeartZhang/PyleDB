import json
import os

def insert(obj, data):
    #{"db":"databasename", "collection":"collection_name" ,"json":{"info":"here"})
    db = data['db']
    collection = data['collection']
    _json = data['json']
    if not os.path.exists(db):
        with open(db, 'wb') as file:
            file.write("{}")

    with open(db, 'rb') as file:
        try:
            stuff = json.loads(file.read())
        except ValueError:
            with open(db, 'wb') as file:
                file.write("{}")
                obj.close()
                return
        if collection not in stuff:
            stuff[collection] = []
        stuff[collection].append(_json)
        with open(db, 'wb') as file:
            file.write(json.dumps(stuff))

    obj.close()
   
