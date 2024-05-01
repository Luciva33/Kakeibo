import tkinter as tk , tkinter.ttk as ttk
import pymysql
import dao

#登録画面のGUI
def create_gui():
    """
    コールバック関数群
    """
    #表示ボタンのコールバック関数
    def select_button():
        root.destroy()
        select_gui()
    #終了ボタンのコールバック関数
    def quit_button():
        root.destroy()
    #登録ボタンが押された時のコールバック関数
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


    """
    空のデータベース接続
    既に登録されている場合は、ddl発行のエラーでexceptブロックで回避
    """
    conn = pymysql.connect(
        host="localhost",
        user="root",
        cursorclass=pymysql.cursors.DictCursor,
        )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kakeibo")
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
    btn2=tk.Button(menuFrame,text="表示",fg="green3",height=2,width=5,command=select_button)
    btn2.pack(anchor="nw",side="left" )
    btn3=tk.Button(menuFrame,text="終了",fg="black",height=2,width=5,command=quit_button)
    btn3.pack(anchor="ne",side="right")
    #電卓機能はまだ未実装
    # btn4=tk.Button(menuFrame,text="電卓",fg="yellow3",height=2,width=5)
    # btn4.pack(anchor="ne",side="right" )

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

    regbtn=tk.Button(root,text="登録",font=("",16),width=10,bg="gray",command=lambda:create_sql(combo.get()))
    regbtn.pack()

    root.mainloop()

"""
表示画面のGUI
"""
def select_gui():
    """
    コールバック関数群
    """
    #登録画面を表示する関数
    def create_button():
        root.destroy()
        create_gui()
    #終了画面を表示する関数
    def quit_button():
        root.destroy()
    #表示ボタンが押された時のコールバック関数
    def select_sql(start,end):
        #Treeviewのアイテムをすべて削除
        tree.delete(*tree.get_children()) 
        # 開始日と終了日が空欄だったらデフォルト値の設定
        if start == "":
            start = "1900-01-01"
        if end == "":
            end = "2100-01-01"
        with dao.connect() as con:
            with con.cursor() as cursor:
                sql="""
                    SELECT acc_date,item_name,amount
                    FROM acc_data as a,item as i
                    WHERE a.item_code = i.item_code AND
                    acc_date BETWEEN '{}' AND '{}'
                    ORDER BY acc_date
                    """.format(start,end)
                cursor.execute(sql)
                items = cursor.fetchall()
                i=0
                for r in items:
                    records=(r["acc_date"],r["item_name"],r["amount"])
                    tree.insert("","end",values=records,tags=i)
                    """
                    tagを追加して、要素を識別
                    tagが奇数か偶数か判定
                    """
                    if i & 1:
                        #tagが奇数の場合のみ、背景色
                        tree.tag_configure(i,background="#ccffff")
                    i+=1
    root = tk.Tk()
    root.title("家計簿アプリ")
    root.geometry("400x500")

    # メニューの設定
    hyouziframe = tk.Frame(root,bd=2,relief="ridge")
    hyouziframe.pack(fill="x")
    btn1=tk.Button(hyouziframe,text="入力",fg="blue3",height=2,width=5,command=create_button)
    btn1.pack(anchor="nw",side="left")
    btn2=tk.Button(hyouziframe,text="表示",fg="green3",height=2,width=5)
    btn2.pack(anchor="nw",side="left" )
    btn3=tk.Button(hyouziframe,text="終了",fg="black",height=2,width=5,command=quit_button)
    btn3.pack(anchor="ne",side="right")
    #電卓機能はまだ未実装
    # btn4=tk.Button(hyouziframe,text="電卓",fg="yellow3",height=2,width=5)
    # btn4.pack(anchor="ne",side="right" )

    #入力画面ラベルの設定
    hyouziLabel=tk.Label(root,text="【表示画面】",font=("",16),height=2)
    hyouziLabel.pack(fill="x")

    #期間選択のラベルエントリーの設定
    frame1=tk.Frame(root,pady=15)
    frame1.pack()
    label2=tk.Label(frame1,font=("",14),text="期間")
    label2.pack(side="left")
    entry1=tk.Entry(frame1,font=("",14),justify="center",width=12)
    entry1.pack(side="left")
    label3=tk.Label(frame1,font=("",14),text="  ～  ")
    label3.pack(side="left")
    entry2=tk.Entry(frame1,font=("",14),justify="center",width=12)
    entry2.pack(side="left")

    #表示ボタンの設定
    btn5 = tk.Button(root,text="表示",
                    font=("",16),
                    width=10,bg="gray",
                    command=lambda:select_sql(entry1.get(),entry2.get()))
    btn5.pack()

    #ツリービューの作成
    tree = ttk.Treeview(root,padding=10)
    #列インデックスの作成
    tree["columns"]=(1,2,3)
    #表スタイルの設定(headingsはつりー形式ではない、通常の表形式)
    tree["show"]="headings"
    #各列の設定(インデックス、オプション(今回は幅を指定))
    tree.column(1,width=100)
    tree.column(2,width=75)
    tree.column(3,width=100)
    #各列のヘッダー設定(インデックス、テキスト)
    tree.heading(1,text="日付")
    tree.heading(2,text="内訳")
    tree.heading(3,text="金額")

    style=ttk.Style()
    style.configure("Treeview",font=("",12))
    style.configure("Treeview.Heading",font=("",14,"bold"))

    with dao.connect() as con:
            with con.cursor() as cursor:
                sql = """
                SELECT  acc_date, item_name,amount
                FROM acc_data as a , item as i
                WHERE a.item_code = i.item_code
                ORDER BY acc_date
                """
                cursor.execute(sql)
                items = cursor.fetchall()

                i=0
                for r in items:
                    records=(r["acc_date"],r["item_name"],r["amount"])
                    tree.insert("","end",values=records,tags=i)
                    """
                    tagを追加して、要素を識別
                    tagが奇数か偶数か判定
                    """
                    if i & 1:
                        #tagが奇数の場合のみ、背景色
                        tree.tag_configure(i,background="#ccffff")
                    i+=1

    tree.pack(fill="x",padx=20,pady=20)
    root.mainloop()

create_gui()