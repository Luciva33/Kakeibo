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

def find_all2():
    result = None
    with connect() as con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM item"
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
    print(find_all())

# def cerate_database():
#     conn = pymysql.connect(
#         host="localhost",
#         user="root",
#         cursorclass=pymysql.cursors.DictCursor,
#         )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS kakeibo")
#     # cursor.execute("SHOW DATABASES ")
#     cursor.close()
#     conn.close()



def cerate_table():
    with connect() as con:
        with con.cursor() as cursor:
            try:
                #itemuテーブルの定義
                ddl="""
                CREATE TABLE item
                (
                item_code INT PRIMARY KEY AUTO_INCREMENT,
                item_name TEXT NOT NULL UNIQUE
                );
                """
               
                #SQLの発行
                cursor.execute(ddl)
                 
                # acc_dataテーブルの定義    
                ddl = """
                CREATE TABLE acc_data
                ( 
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    acc_date DATE NOT NULL,
                    item_code INT NOT NULL,
                    amount INT,
                    FOREIGN KEY(item_code) REFERENCES item(item_code)
                );
                """
                cursor.execute(ddl)
                cursor.execute("INSERT INTO item(item_name) VALUES('食費');")
                cursor.execute("INSERT INTO item(item_name) VALUES('住宅費');")
                cursor.execute("INSERT INTO item(item_name) VALUES('水道光熱費');")
                cursor.execute("INSERT INTO item(item_name) VALUES('税金');")
                cursor.execute("INSERT INTO item(item_name) VALUES('学費');")
                cursor.execute("INSERT INTO item(item_name) VALUES('交通費');")
                cursor.execute("INSERT INTO item(item_name) VALUES('その他');")
                con.commit()  
            except:
                print('エラーもしくはテーブル作成済み')
                pass   
     
# 内訳テーブル(item)にあるitem_nameのタプルを作成する

def createitemname():
    #データベースの接続
    with connect() as con:
        with con.cursor() as cursor:
            li=[]
            #SELECT文でitem_nameを取得、for文で回す
            cursor.execute("SELECT item_name FROM item")
            items = cursor.fetchall()
            for r in items:
                item=r["item_name"]
                li.append([item])
                
            
            # print(li,type(li))
            # print(len(li)) 
        return tuple(li)
            #リスト型のliタプル型に変換、ファンクションに戻す
    


