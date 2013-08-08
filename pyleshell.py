import pyledb as db
import cmd
import sys
import json

class Shell(cmd.Cmd):
    prompt = "PyleDB> "
    pyledb = db.Connect(sys.argv[1])

    def do_find(self, line):
        try:
            line = json.loads(line)
        except:
            print "Invalid Syntax"

        else:
            for collection in line:
                break
            print Shell.pyledb.find(collection, line[collection])

    def do_insert(self, line):
        try:
            line = json.loads(line)
        except:
            print "Invalid Syntax"

        else:
            for collection in line:
                break
            Shell.pyledb.insert(collection, line[collection])

    def do_delete(self, line):
        try:
            line = json.loads(line)
        except:
            print "Invalid Syntax"
        else:
            for collection in line:
                break
            Shell.pyledb.delete(collection, line['collection'])



if __name__ == "__main__":
    d = Shell()
    d.cmdloop()
