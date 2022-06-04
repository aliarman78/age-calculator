from tkinter import *
from datetime import date

root = Tk()
root.title("AGE-CALCULATOR")
root.geometry("400x300")

now_date = str(date.today())

list_today = now_date.split("-")

def calculateAge(user_date,user_month,user_year):
    global today
    global a
    user_date = int(entry_date.get())
    user_month = int(entry_month.get())
    user_year = int(entry_year.get())

    enter_date = int(list_today[2])
    enter_month = int(list_today[1])
    enter_year = int(list_today[0])
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (user_date>enter_date):
        enter_month = enter_month-1
        enter_date = enter_date+month[user_month-1]
    if (user_month>enter_month):
        enter_year = enter_year-1
        enter_month = enter_month+12

    date_result = str(enter_date-user_date)
    month_result = str(enter_month-user_month)
    year_result = str(enter_year-user_year)
    a = Label(root,text="YOU ARE \n"+year_result+" YEARS "+month_result+" MONTHS "+date_result+" DAYS "+ " OLD ",borderwidth=5)
    a.config(font=("Arial",16))
    a.grid(row=5,column=0,columnspan=3)

def clean():
    entry_date.delete(0, END)
    entry_month.delete(0, END)
    entry_year.delete(0, END)
    button = Button(root, text="CLEAR", width=10, command=clean, bg="#E21717", borderwidth=4)

title_label = Label(root,text="AGE CALCULATOR",borderwidth=5)
title_label.config(font=("Arial",28))
title_label.grid(row=0,column=0,columnspan=3)

date_label = Label(root,text="DATE : ",borderwidth=4)
date_label.config(font=("Arial",15))
date_label.grid(row=1,column=0)

month_label = Label(root,text="MONTH : ",borderwidth=5)
month_label.config(font=("Arial",15))
month_label.grid(row=2,column=0)

year_label = Label(root,text="YEAR : ",borderwidth=9)
year_label.config(font=("Arial",15))
year_label.grid(row=3,column=0)

entry_date=Entry(root,width=20,borderwidth=4)
entry_month=Entry(root,width=20,borderwidth=4)
entry_year=Entry(root,width=20,borderwidth=4)

entry_date.grid(row=1,column=2)
entry_month.grid(row=2,column=2)
entry_year.grid(row=3,column=2)

user_date = entry_date.get()
user_month = entry_month.get()
user_year = entry_year.get()

final = Button(root,text="GIVE AGE !!",width=10,anchor=CENTER,command=lambda:calculateAge(user_date,user_month,user_year),bg="#5DA3FA",borderwidth=4)
final.grid(row=4,column=0)

clear_button = Button(root,text="CLEAR",width=10,command=clean, bg="#E21717",borderwidth=4)
clear_button.grid(row=4,column=2)

root.mainloop()
