import tkinter as tk
from tkinter import *
import tkinter.font as fontk
import mysql.connector as sqltor
import datetime
from datetime import date,time
from tkinter import ttk,messagebox

#conecction...........
mycon=sqltor.connect(host='localhost',user='Username',password='Password',database='qtracker')
cursor=mycon.cursor(buffered=True)

#variables
'''All color codes'''
bgcolor='#222222'
bgcolor3='#333333'

#  Function For About
def about():
	about=Tk()
	about.title('About Q Tracker')
	about.geometry('1000x700')
	about.config(bg=bgcolor)
	lbnhead=Label(about,text='Q Tracker',font='Chiller 52',bg=bgcolor,fg='red')
	lbnhead.place(x=410,y=20)
	text='''
	Q tracker {Quarantine Tracker} is a program which helps to manage 
	details in a quarntine center...
	This Program Is Devoloped By:
	      Adithya Krishan XII Jawahar Public School Edava
	      Bharath Krisha XII Jawahar Public School Edava

	 Spcl Thanx to:
	      Priyadershini Miss    Aparna Miss

	    Abhinav     Abhiragh
	      Alisha      Fawaaz
	      Nabeel       Vaishnav
	            Mufeed              StackOverflow
	      ''' 

	lbnabout=Label(about,text=text,font='Chiller 28',bg=bgcolor,fg='white')
	lbnabout.place(x=10,y=90)

	# search for all positive cases
def search_positive():
	ser_pos=Tk()
	ser_pos.title('POSITIVE CASES')
	ser_pos.geometry('1080x590')
	ser_pos.config(bg=bgcolor)
	la=Label(ser_pos,text='ALL POSITIVE CASES',font='bold 32',bg=bgcolor,fg='red')
	la.place(x=320,y=40)
	cmd="select id,name,phone,loc,doa,address from corona where result='{}'".format('positive')
	cursor.execute(cmd)
	mycon.commit()
	dat=cursor.fetchall()
	text1='Id      Name              Phone            loc               Date               Address'
	lb1=Label(ser_pos,text=text1,font='bold 18',bg=bgcolor,fg='blue')
	lb1.place(x=100,y=170)
	py=220
	px=160
	for i in range (0,len(dat)):
		lbn=Label(ser_pos,text=dat[i][0],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=100,y=py)
		lbn=Label(ser_pos,text=dat[i][1],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=160,y=py)
		lbn=Label(ser_pos,text=dat[i][2],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=320,y=py)
		lbn=Label(ser_pos,text=dat[i][3],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=480,y=py)
		lbn=Label(ser_pos,text=dat[i][4],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=610,y=py)
		lbn=Label(ser_pos,text=dat[i][5],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=770,y=py)
		py+=50


		#search by location searching
def search_loc():
	import time as t
	loca=ep.get()
	cmd="select id,name,phone,loc,doa,result from corona where loc='{}'".format(loca)
	cursor.execute(cmd)
	mycon.commit()
	dat=cursor.fetchall()
	py=220
	px=160
	text1='Id      Name              Phone            loc               Date          Result'
	lb1=Label(serl,text=text1,font='bold 18',bg=bgcolor,fg='blue')
	lb1.place(x=100,y=170)
	for i in range (0,len(dat)):
		lbn=Label(serl,text=dat[i][0],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=90,y=py)
		lbn=Label(serl,text=dat[i][1],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=160,y=py)
		lbn=Label(serl,text=dat[i][2],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=320,y=py)
		lbn=Label(serl,text=dat[i][3],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=470,y=py)
		lbn=Label(serl,text=dat[i][4],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=600,y=py)
		lbn=Label(serl,text=dat[i][5],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=740,y=py)
		py+=50

		#search by location GUI
def search_locaction():
	global ep,serl
	serl=Tk()
	serl.title('Search By Location')
	serl.geometry('1080x590')
	lbn=Label(serl,text='Search',font='chiller 32',bg=bgcolor,fg='red')
	lbn.place(x=270,y=20)
	serl.config(bg=bgcolor)
	lbn=Label(serl,text='Enter The Location',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=10,y=90)
	ep=ttk.Entry(serl,width=15,font='chiller 15')
	ep.place(x=230,y=89)
	ep.focus_set()
	but1=Button(serl,text='Print',width=10,height=1,bg=bgcolor3,activebackground=bgcolor,command=search_loc)
	but1.place(x=410,y=90)
	serl.mainloop()

    #search by Id no
def search_id():
	import time as t
	id1=epid.get()
	cmd="select id,name,phone,loc,doa,result,address from corona where id='{}'".format(id1)
	cursor.execute(cmd)
	mycon.commit()
	dat=cursor.fetchall()
	print(dat)
	py=220
	px=160
	text1='  Id      Name              Phone            loc               Date            Result'
	lbn=Label(serl,text='Address',font='bold 18',bg=bgcolor,fg='blue')
	lbn.place(x=10,y=270)
	lb1=Label(serl,text=text1,font='bold 18',bg=bgcolor,fg='blue')
	lb1.place(x=10,y=170)
	for i in range (0,len(dat)):
		lbn=Label(serl,text=dat[i][0],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=10,y=py)
		lbn=Label(serl,text=dat[i][1],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=80,y=py)
		lbn=Label(serl,text=dat[i][2],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=240,y=py)
		lbn=Label(serl,text=dat[i][3],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=390,y=py)
		lbn=Label(serl,text=dat[i][4],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=520,y=py)
		lbn=Label(serl,text=dat[i][5],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=670,y=py)
		lbn=Label(serl,text=dat[i][6],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=110,y=py+50)
		py+=50

    #search by Id GUI
def serid():
	global epid,serl
	serl=Tk()
	serl.title('Search By Id')
	serl.geometry('900x300')
	lbn=Label(serl,text='Search',font='chiller 32',bg=bgcolor,fg='red')
	lbn.place(x=340,y=20)
	serl.config(bg=bgcolor)
	lbn=Label(serl,text='Enter The Id No ',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=50,y=90)
	epid=ttk.Entry(serl,width=15,font='chiller 15')
	epid.place(x=250,y=89)
	epid.focus_set()
	but1=Button(serl,text='Print',width=10,height=2,bg=bgcolor3,activebackground=bgcolor,command=search_id)
	but1.place(x=460,y=90)
	serl.mainloop()

	#search Main Gui

def search():
	ser=Tk()
	ser.title('Search')
	ser.geometry('500x300')
	ser.config(bg=bgcolor)
	lbn=Label(ser,text='Search',font='chiller 32',bg=bgcolor,fg='red')
	lbn.place(x=170,y=20)
	lbn=Label(ser,text='Search by Location',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=70,y=90)
	lbn=Label(ser,text='Search by Id No ',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=70,y=140)
	lbn=Label(ser,text='Search for All + ve\'s',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=70,y=190)
	but1=Button(ser,text='SEARCH',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=search_locaction)
	but1.place(x=290,y=90)
	but2=Button(ser,text='SEARCH',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=serid)
	but2.place(x=290,y=140)
	but3=Button(ser,text='SEARCH',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=search_positive)
	but3.place(x=290,y=190)
	ser.mainloop()

	#Insert New Entries
def insert():
	from datetime import time,datetime
	import time as t
	cmd='select*from id'
	cursor.execute(cmd)
	mycon.commit()
	a=cursor.fetchall()
	b=a
	a=a[0][0]+1
	cmd='update id set count=count+1'
	cursor.execute(cmd)
	mycon.commit()
	a=str(a)
	today=date.today()
	name=ep1.get()
	loc=ep2.get()
	ph=ep3.get()
	ad=ep4.get()
	time=t.localtime()
	time=t.strftime('%H:%M:%S')
	cmd="insert into corona(id,name,loc,address,phone,doa,time) values('{}','{}','{}','{}','{}','{}','{}')".format(a,name,loc,ad,ph,today,time)
	cursor.execute(cmd)
	mycon.commit()
	messagebox.showinfo(title='Id No',message='Id No ='+a)
	add.destroy()


    #Remove an entry
def remo():
	id1=eprem.get()
	res=eprem2.get()
	print(res)
	cmd="update corona set result='{}' where id='{}'".format(res,id1)
	cursor.execute(cmd)
	mycon.commit()
	messagebox.showinfo(title='Remove',message='Removed')
	rem.destroy()


	#Remove GUI
def remove():
	global eprem,eprem2,rem
	rem=Tk()
	rem.title('Remove')
	rem.geometry('300x300')
	rem.config(bg=bgcolor)
	lbn=Label(rem,text='Remove',font='chiller 32',bg=bgcolor,fg='red')
	lbn.place(x=60,y=20)
	lbn=Label(rem,text='Id No',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=20,y=89)
	eprem=ttk.Entry(rem,width=15,font='chiller 15')
	eprem.place(x=100,y=89)
	eprem.focus_set()
	lbn=Label(rem,text='Result',font='chiller 18',bg=bgcolor,fg='white')
	lbn.place(x=20,y=129)
	eprem2=ttk.Entry(rem,width=15,font='chiller 15')
	eprem2.place(x=100,y=129)
	eprem2.focus_set()
	but1=Button(rem,text='Remove',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=remo)
	but1.place(x=90,y=200)
	rem.mainloop()


	#Insert Main GUI
def add():
	global ep1,ep2,ep3,ep4,add
	add=Tk()
	add.title('Add')
	add.geometry('400x400')
	add.config(bg=bgcolor)
	lbhead=Label(add,text='ADD',font='Chiller 38',bg=bgcolor,fg='red')
	lbhead.place(x=140,y=20)
	lbhead=Label(add,text='Name',font='Chiller 18',bg=bgcolor,fg='white')
	lbhead.place(x=50,y=120)
	lbhead=Label(add,text='Locality',font='Chiller 18',bg=bgcolor,fg='white')
	lbhead.place(x=50,y=160)
	lbhead=Label(add,text='Phone',font='Chiller 18',bg=bgcolor,fg='white')
	lbhead.place(x=50,y=200)
	lbhead=Label(add,text='Address',font='Chiller 18',bg=bgcolor,fg='white')
	lbhead.place(x=50,y=240)
	ep1=ttk.Entry(add,width=15,font='chiller 15')
	ep1.place(x=150,y=120)
	ep1.focus_set()
	ep2=ttk.Entry(add,width=15,font='chiller 15')
	ep2.place(x=150,y=160)
	ep2.focus_set()
	ep3=ttk.Entry(add,width=15,font='chiller 15')
	ep3.place(x=150,y=200)
	ep3.focus_set()
	ep4=ttk.Entry(add,width=15,font='chiller 15')
	ep4.place(x=150,y=240)
	ep4.focus_set()
	but1=Button(add,text='Add',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=insert)
	but1.place(x=140,y=300)
	add.mainloop()


	#Main Screen GUI
def main_screen():
	lo.destroy()
	mscreen=Tk()
	mscreen.title('Q Tracker')
	mscreen.geometry('1080x590')
	mscreen.config(bg=bgcolor)
	lbhead=Label(mscreen,text='Q Tracker',font='Chiller 48',bg=bgcolor,fg='white')
	lbhead.place(x=420,y=20)
	lb1=Label(mscreen,text='Today checkouts',font='bold 28',bg=bgcolor,fg='red')
	lb1.place(x=160,y=100)
	today=date.today()
	weekago=today - datetime.timedelta(days=7)
	cmd="select id,name,phone,loc,address from corona where date='{}'".format(weekago)
	cursor.execute(cmd)
	mycon.commit()
	dat=cursor.fetchall()
	py=220
	px=160
	for i in range (0,len(dat)):
		lbn=Label(mscreen,text=dat[i][0],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=150,y=py)
		lbn=Label(mscreen,text=dat[i][1],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=220,y=py)
		lbn=Label(mscreen,text=dat[i][2],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=430,y=py)
		lbn=Label(mscreen,text=dat[i][3],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=590,y=py)
		lbn=Label(mscreen,text=dat[i][4],font='bold 18',bg=bgcolor,fg='black')
		lbn.place(x=720,y=py)
		py+=50
	text1='''    -----------------------------------------------------------
-----------------------------
   -----------'''
	lbn=Label(mscreen,text=text1,font='chiller 18',bg=bgcolor,fg='red')
	lbn.place(x=300,y=py)
	text2='Id      Name                     Phone            Location              Address'
	lb1=Label(mscreen,text=text2,font='chiller 22',bg=bgcolor,fg='blue')
	lb1.place(x=160,y=170)
	but1=Button(mscreen,text='Add',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=add)
	but1.place(x=10,y=170)
	but2=Button(mscreen,text='Remove',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=remove)
	but2.place(x=10,y=240)
	but3=Button(mscreen,text='Search',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=search)
	but3.place(x=10,y=320)
	but4=Button(mscreen,text='About',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=about)
	but4.place(x=10,y=410)
	mscreen.mainloop()
def logscreen():
	global lo
	lo=Tk()
	lo.title('Q-Tracker')
	lo.geometry('900x540')
	lab=Label(lo,text='Quarantine Tracker',font='chiller 32',bg=bgcolor,fg='blue')
	lab.place(x=330,y=10)
	lab=Label(lo,text='Q',font='chiller 140',bg=bgcolor,fg='red')
	lab.place(x=400,y=120)
	lab=Label(lo,text='Tracker',font=('Comic Sans Ms',52),bg=bgcolor,fg='green')
	lab.place(x=310,y=270)
	but1=Button(lo,text='ENTER',width=15,height=2,bg=bgcolor3,activebackground=bgcolor,command=main_screen)
	but1.place(x=400,y=400)
	lo.config(bg=bgcolor)
	lo.mainloop()
if __name__=='__main__':
	logscreen()
