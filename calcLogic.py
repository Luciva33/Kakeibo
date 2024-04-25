import tkinter as tk,dao,test

#ボタンがクリックされた時の処理をコールバック関数として定義

# def callback(name):
#     print("hello world!"+name)

# def text_get():
#     #Entryウィジェットのテキストを読み取るgetメソッド
#     text=entry.get()
#     print(text)

# root=tk.Tk()
# root.geometry("200x200")
# entry= tk.Entry(root,width=10)
# entry.pack()

# #ボタンを作成(rootに配置、テキストの指定、ボタンがクリックされた時に呼び出す関数(コールバック関数)を指定)
# #commndをラムダ形式で記述
# button=tk.Button(root,text="GET",command=text_get)
# button.pack()

# root.mainloop()

def create_sql():
    #日付を読み取る
    acc_data=dateEntry