PyleDB
======

PyleDB is a mini database engine written in Python for when resources are limited and a complex DB engine, such as MongoDB or MySQL isn't needed.

PyleDB uses a NoSQL system.


Example
=======
    
    #First run the PyleDB daemon

    import pyledb
    
    db = pyledb.Connect("database")
    db.insert("collection", {"name":"value"})
    db.find("collection", {"name":"value"})
    db.find("collection", {})
    db.delete("collection", {"name":"value"})


