import tkinter as tk

#カレンダークラスを作成するフレームクラス

class mycalender(tk.Frame):

    def __init__(self,master=None,cnf={},**kw):
        #初期化メソッド
        import datetime
        tk.Frame.__init__(self,master,cnf,**kw)

        #現在の日付を取得
        now = datetime.datetime.now()
        #現在の年と月を属性に追加
        self.year=now.year
        self.month=now.month

        #frame_top部分の作成
        frame_top=tk.Frame(self)
        frame_top.pack(pady=5)
        self.previous_month=tk.Label(frame_top,text="<",font=("",14))
        self.previous_month.pack(side="left",padx=10)
        self.current_year=tk.Label(frame_top,text=self.year,font=("",18))
        self.current_year.pack(side="left")
        self.current_month=tk.Label(frame_top,text=self.month,font=("",18))
        self.current_month.pack(side="left")
        self.next_month=tk.Label(frame_top,text=">",font=("",14))
        self.next_month.pack(side="left",padx=10)

        #frame_week部分の作成
        frame_week=tk.Frame(self)
        frame_week.pack()
        button_mon=d_button(frame_week,text="Mon")
        button_mon.grid(column=0,row=0)
        button_tue=d_button(frame_week,text="Tue")
        button_tue.grid(column=1,row=0)
        button_wed=d_button(frame_week,text="Wed")
        button_wed.grid(column=2,row=0)
        button_thu=d_button(frame_week,text="Thu")
        button_thu.grid(column=3,row=0)        
        button_fri=d_button(frame_week,text="Fri")
        button_fri.grid(column=4,row=0)
        button_sta=d_button(frame_week,text="Sta")
        button_sta.grid(column=5,row=0)        
        button_sun=d_button(frame_week,text="Sun")
        button_sun.grid(column=6,row=0)

        #frame_calenderの部分の作成
        self.frame_calender=tk.Frame(self)
        self.frame_calender.pack()

        #日付部分を作成するメソッドの呼び出し
        self.create_calender(self.year,self.month)

    def create_calender(self,year,month):
        #指定した年、月のカレンダーウィジェットを作成する
        #calenderモジュールのインスタンスを作成
        import calendar
        cal = calendar.Calendar()
        #指定した年月のカレンダーをリストで返す
        days=cal.monthdayscalendar(year,month)

        #日付ボタンを格納する変数をdict型で作成
        self.day={}
        #for文で日付ボタンを生成
        for i in range(0,42):
            c=i-(7*int(i/7))
            r=int(i/7)
            try:
                #日付が0でなかったらボタン作成
                if days[r][c] !=0:
                    self.day[i]=d_button(self.frame_calender,text=days[r][c])
                    self.day[i].grid(column=c,row=r)
            except:
                #月によっては、i=41まで日付がないため日付がないiのエラー回避が必要
                break

#デフォルトボタンクラス
class d_button(tk.Button):
    def __init__(self, master=None,cnf={}, **kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",14),height=2,width=4,relief="flat")


root=tk.Tk()
root.title("Calender App")
mycal=mycalender(root)
mycal.pack()
root.mainloop()