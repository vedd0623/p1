'''we will develop a project for a company to accept details about employees
and display it. We will use 2 different windows for that!
so, lets begin'''

'''lets modify this a little bit usingsome background colors!'''

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *


def f1():
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():
	mw.withdraw()
	vw.deiconify()
	vw_st.delete(1.0,END)
	con=None
	try:
		con=connect("proj.db")
		cursor=con.cursor()
		sql="select * from employee"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=''
		for d in data:
			info+= 'id: ' + str(d[0]) + '	name: ' + str(d[1]) + '	salary: ' + str(d[2]) + '\n'
		vw_st.insert(INSERT,info)	
	except Exception as e:
		showerror('Issue',e)	

def f4():
	vw.withdraw()
	mw.deiconify()

mw=Tk()
mw.title("Main")
mw.geometry("600x600+60+60")
mw.configure(bg='cyan')
f=("arial",20,'bold')

btn_mw_add=Button(mw,text='add details',font=f,command=f1,bg='lightblue')
btn_mw_view=Button(mw,text='view details',font=f,command=f3,bg='lightblue')
btn_mw_add.pack(pady=10)
btn_mw_view.pack(pady=10)

aw=Tk()
aw.title("Add details")
aw.geometry("600x600+60+60")
aw.configure(bg='lightblue')

def add():
	con=None
	try:
		con=connect("proj.db")
		cursor=con.cursor()
		sql="insert into employee values('%d','%s','%f')"
		try:
			id=int(ent_id.get())
		except:
			showerror("Failed","Enter Valid ID")
		if id<0:
			showinfo("Failed","ID Should Be Positive")
		
		try:
			name=ent_name.get()
		except:
			showerror("Failed",'Enter Valid Name')
		
		try:
			salary=float(ent_sal.get())
		except:
			showerror("Failed","Enter Valid Salary")
		if salary<0:
			showerror('Failed','Salary Should Be Positive')
		cursor.execute(sql % (id,name,salary))
		con.commit()
		showinfo('Success','Your Details Have Been Fetched!')
		ent_id.delete(0,END)
		ent_name.delete(0,END)
		ent_sal.delete(0,END)
		ent_id.focus()
	except:
		con.rollback()
		showerror("Issue",'no duplicate id entries')
	finally:
		if con is not None:
			con.close()

lab_id=Label(aw,text='Enter ID',font=f,bg='lightblue')
ent_id=Entry(aw,font=f)
lab_name=Label(aw,text='Enter Name',font=f,bg='lightblue')
ent_name=Entry(aw,font=f)
lab_sal=Label(aw,text='Enter Salary',font=f,bg='lightblue')
ent_sal=Entry(aw,font=f)
btn_sub=Button(aw,text='Submit',font=f,command=add,bg='lightgreen')
btn_main=Button(aw,text="Back To Main",font=f,command=f2,bg='lightgreen')
lab_id.pack(pady=10)
ent_id.pack(pady=10)
lab_name.pack(pady=10)
ent_name.pack(pady=10)
lab_sal.pack(pady=10)
ent_sal.pack(pady=10)
btn_sub.pack(pady=10)
btn_main.pack(pady=10)

vw=Tk()
vw.title("View details")
vw.geometry("600x600+60+60")
vw.configure(bg='lightblue')

vw_st=ScrolledText(vw,font=f,width=35,height=15)
btn_vw_main=Button(vw,text='Back To Main',font=f,command=f4,bg='yellow')
vw_st.pack(pady=10)
btn_vw_main.pack(pady=10)

def exit():
	if askokcancel("Quit","Do You Want To Exit?"):
		mw.destroy()
		aw.destroy()
		vw.destroy()

mw.protocol("WM_DELETE_WINDOW",exit)
aw.protocol("WM_DELETE_WINDOW",exit)
vw.protocol("WM_DELETE_WINDOW",exit)

mw.mainloop()