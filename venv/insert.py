import pymysql
def insert(str1,str2):
        myconn = pymysql.connect(host = "localhost", user = "root",passwd = "170905044",database="python")
        str1="insert into employee(name,email) values ('"+str1+"','"+str2+"')"
        cur = myconn.cursor()
        try:
            db = cur.execute(str1)
            if db==0:
                print("No such record exists")
            else:
             myconn.commit()
             return cur.lastrowid
        except:
           print("error")

        return
