import socket
import threading
import json
import delete
import insert
import find



class PyleDB:
    
    threads = []

    def __init__(self):
        self.cmds = {

            "insert":insert.insert,
            "delete":delete.delete,
            "find":find.find,

                }
        
        self.port = 5897

    def main(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("", self.port))
        sock.listen(5)
        print "Pyle Daemon has started."
        while True:
            obj, addr = sock.accept()
            thread = threading.Thread(target=self.handle, args=(obj, addr[0]))
            PyleDB.threads.append(thread)
            thread.start()

    def handle(self, obj, ip):
        data = obj.recv(1024)
        if data:
            try:
                data = json.loads(data)
            except:
                pass
            else:
                if "cmd" in data:
                    if data['cmd'] in self.cmds:
                        for x in PyleDB.threads:
                            try:
                                x.join()
                            except RuntimeError:
                                break
                        print ip, str(data)
                        safe = False
                        self.cmds[data['cmd']](obj, data['json'])
                        safe = True
                else:
                    obj.close()
if __name__ == "__main__":
    PyleDB().main()
