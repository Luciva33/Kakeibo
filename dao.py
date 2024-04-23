import pymysql

# データベースに接続
def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        # password="root",
        database="kakeibo",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection

# acc_dataテーブルから全件取得
def find_all():
    result = None
    with connect() as con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM acc_data"
            cursor.execute(sql)
            result = cursor.fetchall()
            

    return result

# acc_dataテーブルにデータ１件追加
def insert_one(user):
    with connect() as con:
        with con.cursor() as cursor:
            sql = "INSERT acc_data(acc_date,amount,item_code) VALUES(%s,%s,%s)"
            cursor.execute(sql,(user["acc_date"],user["amount"],user["item_code"]))
        con.commit()



#c.execute("""
#    INSERT INTO acc_data(acc_date.decode("utf-8"),item_code,amount)
#    VALUES({},{},{});""".format(date,code,amount)
#   )

