import tkinter as tk,tkinter.ttk as ttk
import pymysql,dao

"""
ドロップダウンリストはTkinterの拡張モジュールであるTkinter.ttkモジュールを用いる。
ちなみに、ttkにおけるウィジェット名は、コンボボックスである。
"""


# #ルートフレームの作成
# root = tk.Tk()

# #コンボボックスの作成(rootに配置、リストの値を編集不可(readonly)に設定)
# combo =ttk.Combobox(root,state="readonly")
# #リストの値を設定
# combo["values"]=("食費","住宅費","光熱費")
# #デフォルトの値を食費(index=0)に設定
# combo.current(0)
# #コンボボックスの配置
# combo.pack()
# #ボタン作成(コールバックコマンドには、コンボボックスの値を取得し、printする処理を定義)
# button=tk.Button(text="表示",command=lambda:print(combo.get()))
# #ボタンの配置
# button.pack()

# root.mainloop()

def createitemname():
    #データベースの接続
    with dao.connect() as con:
        with con.cursor() as cursor:
            li=[]
            #SELECT文でitem_nameを取得、for文で回す
            cursor.execute("SELECT item_name FROM item")
            items = cursor.fetchall()
            for r in items:
                li.append([r])
            #リスト型のliタプル型に変換、ファンクションに戻す
            print(r)
            print(li)
        return(li) #タプルになってるか？
    

#ボタンが押された時のコールバック関数


def getitemcode(item_name):
    
   
    with dao.connect() as con:
        with con.cursor() as cursor:
            sql=(  f"""
                SELECT item_code FROM item
                WHERE item_name = '{item_name}'
                """)
       
            cursor.execute(sql)
            item_code=cursor.fetchone()
            con.commit()

    #SELECT文の結果をfetchoneメソッドで１つ表示する
    #fethoneメソッドはタプルで帰ってくるので、index0を取得し、出力する←うまくいかなかったので、Dictで返した
  
    print(type(tuple(item_code)))
    print(item_code)
    print(item_name)
   
    

#GUI部分を作成
root=tk.Tk()
combo=ttk.Combobox(root,state='readonly')
combo["values"]=createitemname()
combo.current(0)
combo.pack()

#コールバック関数にgetitemcodeを定義
button=tk.Button(text='表示',command=lambda:getitemcode(combo.get()))
button.pack()

createitemname()

root .mainloop()