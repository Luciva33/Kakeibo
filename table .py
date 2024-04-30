import tkinter as tk, tkinter.ttk as ttk
import pymysql
import dao

root=tk.Tk()

style=ttk.Style()

#ツリービューの全部に対して、フォントサイズの変更
# style.configure("Treeview",font=("",12))

#ツリービューのHeading部分をフォント変更,フォントサイズのみ１４に変更する例
style.configure("Treeview.Heading",font=("",14,"bold"))

#ツリービューの作成
tree = ttk.Treeview(root)


#列インデックスの作成
tree["columns"]=(1,2,3)
#表スタイルの設定(headingsはつりー形式ではない、通常の表形式)
tree["show"]="headings"
#各列の設定(インデックス、オプション(今回は幅を指定))
tree.column(1,width=75)
tree.column(2,width=75)
tree.column(3,width=75)
#各列のヘッダー設定(インデックス、テキスト)
tree.heading(1,text="日付")
tree.heading(2,text="内訳")
tree.heading(3,text="金額")

#レコードの作成
#1番目の引数-配置場所(ツリー形式にしない表設定ではブランクとする)
#2番目の引数-end:表の配置順序を最下部に配置
#(行インデックス番号を指定することもできる)
#3行目の引数-values:レコードの値をタプルで指定する
# tree.insert("","end",values=("2017/5/1","食費",3500))
# tree.insert("","end",values=("2017/5/10","光熱費",7800))
# tree.insert("","end",values=("2017/5/10","住宅費",64000))

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
                print(records)
                print(type(records))
                tree.insert("","end",values=records,tags=i)
                """
                tagを追加して、要素を識別
                tagが奇数か偶数か判定
                """
                if i & 1:
                     #tagが奇数の場合のみ、背景色
                     tree.tag_configure(i,background="#ccffff")
                i+=1
#ツリービューの配置

tree.pack()
root.mainloop()