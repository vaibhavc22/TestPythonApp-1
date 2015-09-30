import psycopg2
import sys

class Postgres:
    def __init__(self):
        self.dbConn = psycopg2.connect(database='AI', user='alex', password='alex') 
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('DELETE FROM "Project1"."State";')
        self.dbConn.commit()      

    def WriteState(self, state):
        self.dbCursor.execute('INSERT INTO "Project1"."State" VALUES ('+ str(state[0][0]) +','+ str(state[0][1]) +','+ str(state[1]) +','+ str(state[2]) +','+ str(state[3]) +','+ str(state[4]) +');')
        self.dbConn.commit()   

    def CloseConnection(self):
        self.dbConn.close()