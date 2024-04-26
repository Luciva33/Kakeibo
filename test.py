import pymysql

def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        # password="root",
        database="kakei",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection

def find_all():
    result = None
    with connect() as con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM acc_data"
            cursor.execute(sql)
            result = cursor.fetchall()

    return result



def insert_two(user):
    with connect() as con:
        with con.cursor() as cursor:
            # sql = "INSERT acc_data(acc_date,amount,item_code) VALUES(%s,%s,%s)"
            sql = "INSERT INTO item(item_code,item_name)VALUES(%s,%s) "
            cursor.execute(sql,(user["item_code"],user["item_name"]))
            cursor.execute("COMMIT;")
        
        con.commit()


