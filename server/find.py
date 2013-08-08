import json
import os

def find(obj, data):
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
                if str(_json) == "{}":
                    obj.send(str(stuff[collection]))
                    obj.close()
                    return
                out = []
                for x in stuff[collection]:
                    app = False
                    for y in _json:
                        if y in x:
                            if _json[y] == x[y]:
                                app = True
                            else:
                                app = False
                                break
                        else:
                            app = False
                            break
                    if app:
                        out.append(x)
    obj.send(str(out))
    obj.close()

