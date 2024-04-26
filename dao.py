import pymysql

# データベースに接続
def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        # password="root",
        database="kakei",
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
            sql = "INSERT INTO acc_data(acc_date,item_code,amount) VALUES(%s,%s,%s)"
            cursor.execute(sql,(user["acc_date"],user["item_code"],user["amount"]))
        con.commit()


#c.execute("""1111
#    INSERT INTO acc_data(acc_date.decode("utf-8"),item_code,amount)
#    VALUES({},{},{});""".format(date,code,amount)
#   )

