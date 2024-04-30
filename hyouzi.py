import tkinter as tk, tkinter.ttk as ttk
import pymysql
import dao,nyuryoku



def select_gui():
    """
    コールバック関数群
    """
    #登録画面を表示する関数
    def create_button():
        root.destroy()
        nyuryoku.create_gui()
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
    btn4=tk.Button(hyouziframe,text="電卓",fg="yellow3",height=2,width=5)
    btn4.pack(anchor="ne",side="right" )

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

