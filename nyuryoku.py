import tkinter as tk , tkinter.ttk as ttk
import pymysql
import dao


conn = pymysql.connect(
    host="localhost",
    user="root",
    cursorclass=pymysql.cursors.DictCursor,
    )
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS kakeibo")
# cursor.execute("SHOW DATABASES ")
cursor.close()
conn.close()

dao.cerate_table()



def getitemcode(item_name):
 with dao.connect() as con:
        with con.cursor() as cursor:
            sql=(  f"""
                SELECT item_code FROM item
                WHERE item_name = '{item_name}'
                """)
       
            cursor.execute(sql)
            item_code=cursor.fetchone()
            itemcode=item_code["item_code"]
            con.commit()
        return itemcode





def create_sql(item_name):
    
   

    #日付を読み取る
    acc_date=dateEntry.get()
    #内訳を読み取る
    item_code=getitemcode(item_name)
    #金額を読み取る
    amount=amountEntry.get()
    user={"acc_date":acc_date,"item_code":item_code,"amount":amount,}
  
    #SQLを発行してDBへ登録
    with dao.connect() as con:
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

label1=tk.Label(root,text="[入力画面]",font=("",14),height=2,bg="green1")
label1.pack(fill="x")

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
# itemsEntry=tk.Entry(itemsFrame,font=("",14),justify="center",width=15)
# itemsEntry.pack(side="left")

# 内訳コンボボックスの作成
combo = ttk.Combobox(itemsFrame, state='readonly',font=("",14),width=13)
combo["values"] = dao.createitemname()
combo.current(0)
combo.pack()

#金額
amountFrame=tk.Frame(root,pady=10)
amountFrame.pack()
amountLabel=tk.Label(amountFrame,font=("",14),text="金額")
amountLabel.pack(side="left")
amountEntry=tk.Entry(amountFrame,font=("",14),justify="center",width=15)
amountEntry.pack(side="left")

#登録ボタンの設定

regbtn=tk.Button(root,text="登録",font=("",16),width=10,bg="blue2",command=lambda:create_sql(combo.get()))
regbtn.pack()

# root2=tk.Tk()
# root2.title("電卓")
# root2.geometry("400x400")
# root2.mainloop()

"""
アプリの処理
"""




# print(dao.find_all())
# print(dao.find_all2())



root.mainloop()
