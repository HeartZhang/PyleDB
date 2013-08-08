import socket
import json

#{"db":"databasename", "collection":"collection_name" ,"json":{"info":"here"})


class Connect:
    def __init__(self, db, ip="", port=5897):
        self.db = db
        self.ip = ip
        self.port = port

    def _doit(self, cmd, collection, data):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        sock.send(json.dumps({"cmd":cmd, "json":{"db":self.db, "collection":collection, "json":data}}))
        data = sock.recv(102400000)
        if data:
            return eval(data)

    def delete(self, collection, data):
        self._doit("delete", collection, data)

    def find(self, collection, data):
        data = self._doit("find", collection, data)
        if data is None:
            return []
        else:
            return data

    def insert(self, collection, data):
        self._doit("insert", collection, data)
