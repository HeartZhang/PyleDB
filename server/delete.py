import json
import os

def delete(obj, data):
    #{"db":"databasename", "collection":"collection_name" ,"json":{"info":"here"})
    db = data['db']
    collection = data['collection']
    _json = data['json']

    if not os.path.exists(db):
        obj.close()
        return
    else:
        with open(db, 'rb') as file:
            stuff = json.loads(file.read())
            if collection not in stuff:
                obj.close()
                return
            else:
                for x in stuff[collection]:
                    remove = False
                    for y in _json:
                        if y in x:
                            if _json[y] == x[y]:
                                remove = True
                            else:
                                remove = False
                                break
                    if remove:
                        stuff[collection].remove(x)
                with open(db, 'wb') as file:
                    file.write(json.dumps(stuff))

    obj.close()
