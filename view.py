import pymysql
def view(id1):
        myconn = pymysql.connect(host = "localhost", user = "root",passwd = "170905044",database="python")
        str1="select * from employee where id ="+id1
        cur = myconn.cursor()
        try:
            db = cur.execute(str1)
            if db==0:
                print("No such record exists")
                return
        except:
           print("error")
        for x in cur:
            print(x)
            print("hi")

