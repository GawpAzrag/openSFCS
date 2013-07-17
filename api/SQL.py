import psycopg2

from dbConfig import dbConfig


class SQL:

    def conn(self):  
        self.cnx = psycopg2.connect(dbname=dbConfig['NAME'],
                                    user=dbConfig['USER'],
                                    host=dbConfig['HOST'],
                                    password=dbConfig['PASSWORD'],
                                    port=dbConfig['PORT']) 
        self.cur = self.cnx.cursor()
    
    
    def read(self,s,v):  
        self.cur.execute(s,v)
        data = self.cur.fetchall()
        return data
        
    def execute(self,s,v):      
        self.cur.execute(s,v)
    
    def commit(self): 
        self.cnx.commit()
        
    def close(self):
        self.cur.close()
        self.cnx.close()

def quickSqlRead(s,v):  
    sql = SQL()
    sql.conn()
    data = sql.read(s,v)
    sql.close()
    return data
    
def quickSqlWrite(s,v):
    sql = SQL()
    sql.conn()
    sql.execute(s,v)
    sql.commit()
    sql.close()