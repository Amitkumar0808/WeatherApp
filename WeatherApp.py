from tkinter import *
from tkinter import  ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3582913f081af70564f5d6932d35d496").json()
    w__label1.config(text=data["weather"][0]["main"])
    wb__label1.config(text=data["weather"][0]["description"])
    temp__label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per__label1.config(text=data["main"]["pressure"])






win = Tk()
win.title("Weatheer App")
win.config(bg ="blue")
win.geometry("1400x1400")


name__label =Label(win,text="Weather App",font=("Time New Roman",40,"bold"),bg='blue')
name__label.place(x=550,y=40,height=50,width=450)

city_name = StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com =ttk.Combobox(win,text="Weather App", values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=550,y=120,height=50,width=450)


w__label =Label(win,text="Weather climate",font=("Time New Roman",20,"bold"),bg='blue')
w__label.place(y=280,height=40,width=230,x=500)

w__label1 =Label(win,text="",font=("Time New Roman",20,"bold"))
w__label1.place(y=280,height=40,width=230,x=830)

wb__label =Label(win,text="Weather Description",font=("Time New Roman",18,"bold"),bg='blue')
wb__label.place(y=330,height=40,width=250,x=500)

wb__label1 =Label(win,text="",font=("Time New Roman",18,"bold"))
wb__label1.place(y=330,height=40,width=230,x=830)


temp__label =Label(win,text="Temperature",font=("Time New Roman",20,"bold"),bg='blue')
temp__label.place(y=380,height=40,width=230,x=500)

temp__label1 =Label(win,text="",font=("Time New Roman",20,"bold"))
temp__label1.place(y=380,height=40,width=230,x=830)


per__label =Label(win,text="Pressure",font=("Time New Roman",20,"bold"),fg='black',bg='blue')
per__label.place(y=430,height=40,width=230,x=500)

per__label1 =Label(win,text="",font=("Time New Roman",20,"bold"))
per__label1.place(y=430,height=40,width=230,x=830)


done_button = Button(win, text="Done",font=("Time New Roman",20,"bold"),fg='white',bg='blue',command=data_get)

done_button.place(y=200,height=50,width=100,x=730)

win.mainloop()