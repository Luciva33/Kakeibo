import tkinter as tk
import pymysql
import dao


def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        # password="root",
        database="kakei",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


conn = pymysql.connect(
        host="localhost",
        user="root",
        charset='utf8mb4',
        # password="root",
        database="kakei",
        cursorclass=pymysql.cursors.DictCursor,
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS kakei")
cursor.execute("SHOW DATABASES ")
cursor.close()
conn.close()
for x in cursor:
    print(x)

# with connect() as con:
#    with con.cursor() as cursor:
#         try:
#             #itemuテーブルの定義
#             ddl="""
#             CREATE TABLE item
#             (
#             item_code INTEGER PRIMARY KEY AUTOINCREMENT,
#             item_name TEXT NOT NULL UNIQUE
#             );
#             """
#             #SQLの発行
#             cursor.execute(ddl)
#             # acc_dataテーブルの定義    
#             ddl = """
#             CREATE TABLE acc_data
#             ( 
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 acc_date DATE NOT NULL,
#                 item_code INTEGER NOT NULL,
#                 amount INTEGER,
#                 FOREIGN KEY(item_code) REFERENCES item(item_code)
#             );
#             """
#             cursor.execute(ddl)
#             cursor.execute("INSERT INTO item(item_name) VALUES('食費');")
#             cursor.execute("INSERT INTO item(item_name) VALUES('住宅費');")
#             cursor.execute("INSERT INTO item(item_name) VALUES('光熱費');")
#         except:
#             pass    


def create_sql():
    
    #日付を読み取る
    acc_date=dateEntry.get()
    #内訳を読み取る
    item_code=itemsEntry.get()
    #金額を読み取る
    amount=amountEntry.get()
    user={"acc_date":acc_date,"item_code":item_code,"amount":amount,}
    #SQLを作成して出力
    # print("""
    # INSERT INTO acc_data(acc_date,item_code_,amount)
    # VALUES('{}',{},{});
    # """.format(acc_date,item_code,amount))

    #SQLを発行してDBへ登録
    with connect() as con:
        with con.cursor() as cursor:
            try:    
                dao.insert_one(user)            
                print("1件登録しました")
                #ドメインエラーなどにより登録できなかった場合のエラー処理    
            except:
                print("エラー!登録できませんでした")


root = tk.Tk()
root.title("家計簿アプリ")
root.geometry("300x280")


"""
メニューの設定
"""

menuFrame = tk.LabelFrame(root,bd=2,relief="ridge",text="menu")
menuFrame.pack(fill="x")

btn1=tk.Button(menuFrame,text="入力",fg="blue3",height=2,width=5)
btn1.pack(anchor="nw",side="left")
btn2=tk.Button(menuFrame,text="表示",fg="green3",height=2,width=5)
btn2.pack(anchor="nw",side="left" )
btn3=tk.Button(menuFrame,text="終了",fg="black",height=2,width=5)
btn3.pack(anchor="ne",side="right")
btn4=tk.Button(menuFrame,text="電卓",fg="yellow3",height=2,width=5)
btn4.pack(anchor="ne",side="right" )


#入力画面ラベル

label1=tk.Label(root,text="[入力画面]",font=14,bg="green1")
label1.pack()

#日付のラベルとエントリー

dateFrame =tk.Frame(root,pady=10) 
dateFrame.pack()
dateLabel=tk.Label(dateFrame,font=("",14),text="日付")
dateLabel.pack(side="left")
dateEntry = tk.Entry(dateFrame,font=("",14),justify="center",width=15)
dateEntry.pack(side="left")

#内訳のラベルとエントリーの設定
itemsFrame=tk.Frame(root,pady=10)
itemsFrame.pack()
itemsLabel=tk.Label(itemsFrame,font=("",14),text="内訳")
itemsLabel.pack(side="left")
itemsEntry=tk.Entry(itemsFrame,font=("",14),justify="center",width=15)
itemsEntry.pack(side="left")

#金額
amountFrame=tk.Frame(root,pady=10)
amountFrame.pack()
amountLabel=tk.Label(amountFrame,font=("",14),text="金額")
amountLabel.pack(side="left")
amountEntry=tk.Entry(amountFrame,font=("",14),justify="center",width=15)
amountEntry.pack(side="left")

#登録ボタンの設定

regbtn=tk.Button(root,text="登録",font=("",16),width=10,bg="blue2",command=create_sql)
regbtn.pack()



# root2=tk.Tk()
# root2.title("電卓")
# root2.geometry("400x400")
# root2.mainloop()


#アプリの処理

root.mainloop()
