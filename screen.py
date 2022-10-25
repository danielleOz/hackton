import tkinter
from tkinter import *
import volenteer
app = Tk()
app.title("volt")
app.geometry("700x700+700+100")
app.configure(bg = "pink")

def print_stars():
 print ("**************")

# lblNum = Label(app, text="Please enter a number:", height = 10)
# lblNum.pack()
lbl_start=Label(app, text="welcome to VOLT:",font=('Arial Bold',30), bg="pink",fg='white')
lbl_start.grid(row=0, column=1)

lbl_name=Label(app,text="enter your name:",height=10,width=30, bg="pink",fg='white',anchor=W)
lbl_name.grid(row=1, column=0)

lbl_id=Label(app,text="enter your id:",height=10,width=30, bg="pink",fg='white',anchor=W)
lbl_id.grid(row=2, column=0)

lbl_skills=Label(app,text="enter your skills:",height=10,width=30, bg="pink",fg='white',anchor=W)
lbl_skills.grid(row=3, column=0)

name_enter=Entry(app)
name_enter.grid(row=1, column=1)

id_enter=Entry(app)
id_enter.grid(row=2, column=1)

skil_enter=Entry(app)
skil_enter.grid(row=3,column=1)


# decNum=Entry(app)
# decNum.pack()
def save_date():
    name=name_enter.get()
    name_enter.delete(0, END)
    id=id_enter.get()
    id_enter.delete(0,END)
    skill=skil_enter.get()
    skil_enter.delete(0,END)
    # volenteer.create_vol(name,id,skill)
    vol=volenteer.create_vol(name,id,skill)
    print(vol)



    # print(name,id,skill)


btnClick = Button(app, text = "click", width = 10,command=save_date)
btnClick.grid(row=5, column=0)

app.mainloop()
