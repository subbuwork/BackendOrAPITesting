import pymysql

class dbconnect():
    def __init__(self):
        pass

    def __connnect__(self,db):
        """
        :param db:
        :return:
        """
        host ='127.0.0.1'
        conn = pymysql.connect(host=host,port=3306,user='user1',db=db)

        return conn

    def test_select(self, db,query):
        conn = self.__connnect__(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col)) #Converting ecach value into string
        all_rows.append(row)

        cur.close() # Clearing cursor
        conn.close() # Closing connection
    def test_update(self,db,query):
        """
        :param db:
        :param query:
        :return:
        """
        # Creating db conneciton
        conn = self.__connnect__(db)
        cur = conn.cursor()

        #Execute query
        result = cur.execute(query)
        conn.commit()

        #Closing cursor and connection

        cur.close()
        conn.close()
        