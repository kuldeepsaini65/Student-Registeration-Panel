'''
Project Name - Student Registration Panel 
This Project is Developed by Kuldeep Saini

Profile - https://www.github.com/kuldeepsaini65


Used Module -> 1) Tkinter
               2) PIL
               3) sqllite3 

All the details filled up by the user is saved in an DBMS file named < student_data.db >

'''

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

def sql_connect():
    global cursor
    global connect
    connect = sqlite3.connect("/student_data.db")
    cursor = connect.cursor()
    cursor.execute("create table if not exists student_data(reg_id integer primary key AUTOINCREMENT, name TEXT, age integer ,gender text,course TEXT);")
    connect.commit()

def show_data():
    
    data_window = Tk()
    data_window.geometry("550x700")
    data_window.title("Student Records")
    data_window.maxsize(550,700)
    data_window.minsize(550,700)


   
    """
    
    Labels for name

    """

    heading = Label(data_window, text="Student Records", bg="lightblue",font="times 18 bold")
    heading.grid(row=0,column=0, columnspan=20,ipadx=189,ipady=10)
    
    
    name = Label(data_window, text="Name" ,font="times 18 bold")
    name.grid(row=1,column=0,ipadx=30,ipady=10)

    age = Label(data_window, text="Age" ,font="times 18 bold")
    age.grid(row=1,column=1,ipadx=30,ipady=10)

    gender = Label(data_window, text="Gender" ,font="times 18 bold")
    gender.grid(row=1,column=2,ipadx=30,ipady=10)

    course1 = Label(data_window, text="Course" ,font="times 18 bold")
    course1.grid(row=1,column=3,ipadx=30,ipady=10)
    

    cursor.execute("select * from student_data")
    connect.commit()
    data = cursor.fetchall()
    count = 2
    for row in data:

        name_label = Label(data_window, text=row[1],  font="times 14 ")
        name_label.grid(row=count, column=0,pady=3)

        age_label = Label(data_window, text=row[2],  font="times 14 ")
        age_label.grid(row=count, column=1,pady=3)
        
        gender_label = Label(data_window, text=row[3],  font="times 14 ")
        gender_label.grid(row=count, column=2,pady=3)
        
        course_label = Label(data_window, text=row[4],  font="times 14 ")
        course_label.grid(row=count, column=3,pady=3)

        count+=1


    data_window.mainloop()

def insert_data():
    name = store_name.get()
    age = store_age.get()
    gender = store_gender.get()
    course1 = course_value1.get()
    

    row_data = (name, age, gender, course1)

    cursor.execute('insert into student_data(name, age, gender, course) values(?,?,?,?);',row_data)
    connect.commit()
    print("Data Inserted")


root = Tk()
root.geometry("550x680")
root.title("Login Pannel")

'''
    Logo
'''
canvas = Canvas(root, width = 300, height = 350)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("img\login_100.png"))
canvas.create_image(107, 10, anchor=NW, image=img)

'''
    Details Pannel
'''
store_name = StringVar()
store_age = StringVar()
store_gender = StringVar()
course_value1 = StringVar()


sql_connect()
'''       
***    Heading       ***
'''
heading = Label(root,text="Student Registration Pannel",font=('times',20)).place(x=127,y=113)


name_label = Label(root,text="Enter Name ",font=("times",16)).place(x=45,y=215)
name_entry = Entry(root,textvariable=store_name,font="lucida 13 italic").place(x=275,y=220)

age_label = Label(root,text="Enter Age ",font=("times",16)).place(x=45,y=260)
age_entry = Entry(root,textvariable=store_age,font="lucida 12 italic").place(x = 275,y = 265)


gender_label = Label(root,text="Select Your Gender ",font=("times",16)).place(x=45,y=310)
gender_entry = Radiobutton(root,text="Male",font="lucida 12 ",variable=store_gender, value="male")
gender_entry.place(x = 265,y = 310)
gender_entry = Radiobutton(root,text="Female",font="lucida 12 ",variable=store_gender, value="female")

gender_entry.place(x = 395,y = 310)
store_gender.set("male")

course_label = Label(root,text="Select  Course ",font=("times",16)).place(x=45,y=360)

course = Radiobutton(root,text="Python",font="lucida 13",variable=course_value1,value="python")
course.place(x=245,y=356)

course = Radiobutton(root,text="Java",font="lucida 13",variable=course_value1,value="java")
course.place(x=325,y=356)

course = Radiobutton(root,text="PHP",font="lucida 13",variable=course_value1, value= "php")
course.place(x=395,y=356)
course_value1.set("python")

'''
        ***  Buttons   ***
'''
submit_button = Button(root, text="Submit Now",font="times 13 ",bg="mediumpurple1",width=15,borderwidth=4,command=insert_data)
submit_button.place(x=45,y=434)


show_data_button = Button(root, text="Show Data",font="times 13 ",bg="mediumpurple1",width=15,borderwidth=4,command=show_data)
show_data_button.place(x=345,y=434)

exit_button = Button(root, text="Close Window", bg="firebrick1",font="times 13 ",width=15,borderwidth=4,command=root.destroy)
exit_button.place(x=195,y=534)

footer_label = Label(root, text="Developed By  @kuldeepSaini65",bg="lightblue",font="lucida 13")
footer_label.pack(side=BOTTOM,ipadx=150,ipady=10)

root.mainloop()