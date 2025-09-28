import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,Email text,Gender text,state text,Address text,DOB text,Contact text,City text,Course text,AdmissionDate text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(Rid INTEGER PRIMARY KEY AUTOINCREMENT,Roll text,Name text,Course text,Marks_ob text,FullMarks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Register(Rid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,LName text,Contact text,Email text,Password text,CPassword text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Login(Lid INTEGER PRIMARY KEY AUTOINCREMENT,Email text,Password text)")
    con.commit()



    con.close()


    
create_db()