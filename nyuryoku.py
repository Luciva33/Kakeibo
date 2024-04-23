import tkinter as tk

root = tk.Tk()
root.title("家計簿アプリ")
root.geometry("300x300")

btn1=tk.Button(root,text="入力",fg="blue3",height=2,width=5)
btn1.pack(anchor="nw",side="left")
btn2=tk.Button(root,text="表示",fg="green3",height=2,width=5)
btn2.pack(anchor="nw",side="left" )
btn3=tk.Button(root,text="終了",fg="black",height=2,width=5)
btn3.pack(anchor="ne",side="right")
btn4=tk.Button(root,text="電卓",fg="yellow3",height=2,width=5)
btn4.pack(anchor="ne",side="right" )


"""
画面同時にできそうだ
root2=tk.Tk()
root2.title("家計簿アプリ")
root2.geometry("400x400")
root2.mainloop()
"""

#アプリの処理

root.mainloop()
