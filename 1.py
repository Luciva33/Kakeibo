import calendar
import tkinter as tk
cal = calendar.Calendar()
days = cal.monthdayscalendar(2017,6)

# widget.grid(column=0,row=0)

root = tk.Tk()
day = {}
for i in range(0,42):
    c = i - (7 * int(i/7))
    r = int(i/7)
    try:
        if days[r][c] != 0 :
            day[i] = tk.Button(root,text=days[r][c])
            day[i].grid(column = c, row = r)
    except:
        break

root.mainloop()