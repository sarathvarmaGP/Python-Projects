from tkinter import *
import tkinter.messagebox
import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='', db='employee')
cursor=db.cursor()

access=Tk()
access.geometry('900x500')
access.title('Employee Details')
access.configure(bg='black')

def calculate():
    emp_As.set(emp_salary.get()*12)

def add():
    id=emp_id.get()
    name=emp_name.get()
    role=emp_role.get()
    salary=emp_salary.get()
    As=emp_As.get()
    cursor.execute('insert into details values(%s,%s,%s,%s,%s)',[id,name,role,salary,As])
    db.commit()
    tkinter.messagebox.showinfo('Employee details', 'Details Added')
def view():
    id=emp_id.get()
    cursor.execute('select * from details where EmpId=%s', [id])
    data = cursor.fetchone()
    if data != None:
        emp_name.set(data[1])
        emp_role.set(data[2])
        emp_salary.set(data[3])
        emp_As.set(data[4])
    else:
        tkinter.messagebox.showinfo('Employee details', 'No Data')
def update():
    id = emp_id.get()
    role = emp_role.get()
    salary = emp_salary.get()
    As = emp_As.get()
    cursor.execute('update details set EmpRole=%s, EmpSalary=%s, EmpAs=%s where EmpId=%s', [role, salary, As, id])
    db.commit()
    tkinter.messagebox.showinfo('Employee details', 'Details Updated')
def delete():
    id=emp_id.get()
    cursor.execute('delete from details where EmpId=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Employee Details', 'Details Deleted')
def clear():
    emp_id.set('')
    emp_name.set('')
    emp_role.set('')
    emp_salary.set('')
    emp_As.set('')
def overall():
    global viewpage
    viewpage = Toplevel(access)
    viewpage.geometry('1000x400')
    viewpage.title('Employees List')
    viewpage.configure(bg='black')
    cursor.execute('select * from details')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewpage, text='Emp Id', font=('calibri', 15, 'bold'),fg='red', bg='black').grid(row=0, column=0)
    Label(viewpage, text='Emp Name', font=('calibri', 15, 'bold'),fg='red', bg='black').grid(row=0, column=1)
    Label(viewpage, text='Emp Role', font=('calibri', 15, 'bold'),fg='red', bg='black').grid(row=0, column=2)
    Label(viewpage, text='Emp Salary', font=('calibri', 15, 'bold'),fg='red', bg='black').grid(row=0, column=3)
    Label(viewpage, text='Emp As', font=('calibri', 15, 'bold'),fg='red', bg='black').grid(row=0, column=4)
    for i in range(rows):
        for j in range(cols):
            s = Entry(viewpage, font=('calibri', 12))
            s.grid(row=i + 1, column=j)
            s.insert(END, data[i][j])



Label(access, text='Employee Details', font=('calibri', 25, 'bold'), fg='red', bg='black').place(x=300, y=10)

emp_id_label=Label(access, text='Employee Id', font=('calibri', 25),fg='white', bg='black')
emp_id_label.place(x=100, y=80)
emp_id=StringVar()
emp_id_entry=Entry(access, textvariable=emp_id, font=('calibri', 20))
emp_id_entry.place(x=450, y=80)

emp_name_label=Label(access, text='Employee Name', font=('calibri', 25),fg='white', bg='black')
emp_name_label.place(x=100, y=140)
emp_name=StringVar()
emp_name_entry=Entry(access, textvariable=emp_name, font=('calibri', 20))
emp_name_entry.place(x=450, y=140)

emp_role_label=Label(access, text='Employee Role', font=('calibri', 25),fg='white', bg='black')
emp_role_label.place(x=100, y=200)
emp_role=StringVar()
emp_role_entry=Entry(access, textvariable=emp_role, font=('calibri', 20))
emp_role_entry.place(x=450, y=200)

emp_salary_label=Label(access, text='Employee Salary', font=('calibri', 25),fg='white', bg='black')
emp_salary_label.place(x=100, y=260)
emp_salary=IntVar()
emp_salary_entry=Entry(access, textvariable=emp_salary, font=('calibri', 20))
emp_salary_entry.place(x=450, y=260)

emp_As_label=Label(access, text='Employee AnnualSalary', font=('calibri', 25),fg='white', bg='black')
emp_As_label.place(x=100, y=320)
emp_As=IntVar()
emp_As_entry=Entry(access, textvariable=emp_As, font=('calibri', 20))
emp_As_entry.place(x=450, y=320)

but_cal=Button(access, text='Calcuate', command=calculate, font=('calibri', 12, 'bold'), fg='white', bg='blue', width='8', height='1')
but_cal.place(x=740, y=260)

but_add=Button(access, text='Add',command=add, font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_add.place(x=100, y=400)

but_view=Button(access, text='View',command=view, font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_view.place(x=230, y=400)

but_update=Button(access, text='Update',command=update, font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_update.place(x=360, y=400)

but_del=Button(access, text='Delete',command=delete, font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_del.place(x=490, y=400)

but_clr=Button(access, text='Clear',command=clear , font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_clr.place(x=620, y=400)

but_ovr=Button(access, text='OverAll',command=overall, font=('calibri', 15, 'bold'), fg='white', bg='blue', width='10', height='1')
but_ovr.place(x=750, y=400)

access.mainloop()