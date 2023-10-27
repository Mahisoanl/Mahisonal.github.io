from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlanydb

class studentClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1100x500+220+130")
		self.root.title("Quizhack System | Developed by Mahi")
		self.root.config(bg="white")
		self.root.focus_force()
		#========All Veriables===========================
		self.var_searchby=StringVar()
		self.var_searchtxt=StringVar()

		self.var_s_code=StringVar()
		self.var_s_name=StringVar()
		#self.var_s_address=StringVar()
		self.var_s_user=StringVar()
		self.var_s_password=StringVar()
		self.var_s_gender=StringVar()
		self.var_s_serial_no=IntVar()

		#==============searchFrame=======================
		SearchFrame=LabelFrame(self.root,text="Search Student",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
		SearchFrame.place(x=250,y=20,width=600,height=70)

		#================options=========================
		cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","s_name","s_user"),state='readonly',justify=CENTER,font=("goudy old style",15))
		cmb_search.place(x=10,y=10,width=180)
		cmb_search.current(0)

		txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=10)
		btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

		#======== Title=================
		title=Label(self.root,text="Student Details",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=50,y=100,width=1000)

		#======== Contents=================
		lbl_s_code=Label(self.root,text="Student Code",font=("goudy old style",15),bg="white").place(x=50,y=150)
		lbl_s_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=180)
		lbl_s_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=210)
		lbl_s_user=Label(self.root,text="User",font=("goudy old style",15),bg="white").place(x=50,y=290)
		lbl_s_password=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=50,y=320)
		lbl_s_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=50,y=350)
		lbl_s_serial_no=Label(self.root,text="Serial No.",font=("goudy old style",15),bg="white").place(x=650,y=350)

		txt_s_code=Entry(self.root,textvariable=self.var_s_code,font=("goudy old style",15),bg="white").place(x=200,y=150,width=120)
		txt_s_name=Entry(self.root,textvariable=self.var_s_name,font=("goudy old style",15),bg="white").place(x=200,y=180)
		#txt_s_address=Text(self.root,font=("goudy old style",15),bg="white").place(x=200,y=210,width=550,height=70)
		#txt_s_address=Entry(self.root,textvariable=self.var_s_address,font=("goudy old style",15),bg="white").place(x=200,y=210,width=850)
		
		self.txt_s_address=Text(self.root,font=("goudy old style",15),bg="white")
		self.txt_s_address.place(x=200,y=210,width=550,height=70)

		txt_s_user=Entry(self.root,textvariable=self.var_s_user,font=("goudy old style",15),bg="white").place(x=200,y=290,width=120)
		txt_s_password=Entry(self.root,textvariable=self.var_s_password,font=("goudy old style",15),bg="white").place(x=200,y=320,width=120)
		#txt_s_gender=Entry(self.root,textvariable=self.var_s_gender,font=("goudy old style",15),bg="white").place(x=200,y=270,width=120)
		cmb_s_gender=ttk.Combobox(self.root,textvariable=self.var_s_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("goudy old style",15))
		cmb_s_gender.place(x=200,y=350,width=120)
		cmb_s_gender.current(0)
		txt_s_serial_no=Entry(self.root,textvariable=self.var_s_serial_no,font=("goudy old style",15),bg="white").place(x=800,y=350,width=120)

		
		

		#========Buttons=================
		btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=200,y=390,width=150,height=30)
		btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=380,y=390,width=150,height=30)
		btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=560,y=390,width=150,height=30)
		btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=740,y=390,width=150,height=30)
		btn_next=Button(self.root,text="Next",command=self.next,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=920,y=390,width=150,height=30)

		#==============Student Details=======================
		student_frame=Frame(self.root,bd=3,relief=RIDGE)
		student_frame.place(x=0,y=420,relwidth=1,height=80)
		scrolly=Scrollbar(student_frame,orient=VERTICAL)
		scrollx=Scrollbar(student_frame,orient=HORIZONTAL)

		self.StudentTable=ttk.Treeview(student_frame,columns=("s_code","s_name","s_address","s_user","s_password","s_gender","s_serial_no"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM,fill=X)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.config(command=self.StudentTable.xview)
		scrolly.config(command=self.StudentTable.yview)

		self.StudentTable.heading("s_code",text="Code")
		self.StudentTable.heading("s_name",text="Name")
		self.StudentTable.heading("s_address",text="Address")
		self.StudentTable.heading("s_user",text="User")
		self.StudentTable.heading("s_password",text="Password")
		self.StudentTable.heading("s_gender",text="Gender")
		self.StudentTable.heading("s_serial_no",text="Serial No.")
		self.StudentTable["show"]="headings"

		
		self.StudentTable.column("s_code",width=90)
		self.StudentTable.column("s_name",width=90)
		self.StudentTable.column("s_address",width=90)
		self.StudentTable.column("s_user",width=90)
		self.StudentTable.column("s_password",width=90)
		self.StudentTable.column("s_gender",width=90)
		self.StudentTable.column("s_serial_no",width=90)
		self.StudentTable.pack(fill=BOTH,expand=1)
		self.StudentTable.bind("<ButtonRelease-1>",self.get_data)

		self.show()



#============================================================
	def add(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()
		try:
			if self.var_s_code.get()=="":
				messagebox.showerror("Error","Student Code must be required",parent=self.root)
			else:
				cur.execute("SELECT * FROM student where s_code=?",(self.var_s_code.get(),))
				row=cur.fetchone()
				if row!=None:
					messagebox.showerror("Error","This Student Code already assigned. try diffrent",parent=self.root)
				else:
					cur.execute("insert into student (s_code,s_name,s_address,s_user,s_password,s_gender,s_serial_no) values(?,?,?,?,?,?,?)",(
										self.var_s_code.get(),
										self.var_s_name.get(),
										#self.var_s_address.get(),
										self.txt_s_address.get('1.0',END),
										self.var_s_user.get(),
										self.var_s_password.get(),
										self.var_s_gender.get(),
										self.var_s_serial_no.get()
					))
					con.commit()
					con.close()
					messagebox.showinfo("Success","Student Added Succussfully",parent=self.root)
					self.show()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


	def show(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			cur.execute("SELECT * FROM student")
			rows=cur.fetchall()
			self.StudentTable.delete(*self.StudentTable.get_children())
			for row in rows:
				self.StudentTable.insert('',END,values=row)
			con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


	def get_data(self,ev):
		f=self.StudentTable.focus()
		content=(self.StudentTable.item(f))
		row=content['values']
		#print(row)
		self.var_s_code.set(row[0])
		self.var_s_name.set(row[1])
		self.txt_s_address.delete('1.0',END)
		self.txt_s_address.insert(END,row[2])
		self.var_s_user.set(row[3])
		self.var_s_password.set(row[4])
		self.var_s_gender.set(row[5])			
		self.var_s_serial_no.set(row[6])	

	def update(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()

		try:
			if self.var_s_code.get()=="":
				messagebox.showerror("Error","Student Code must be required",parent=self.root)
			else:
				cur.execute("SELECT * FROM student where s_code=?",(self.var_s_code.get(),))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid Student code",parent=self.root)
				else:
					cur.execute("update student set s_name=?,s_address=?,s_user=?,s_password=?,s_gender=?,s_serial_no=?where s_code=?",(
											self.var_s_name.get(),
											self.txt_s_address.get('1.0',END),
											self.var_s_user.get(),
											self.var_s_password.get(),
											self.var_s_gender.get(),
											self.var_s_serial_no.get(),
											self.var_s_code.get(),
					))
					con.commit()
					con.close()
					messagebox.showinfo("Success","Student updated Succussfully",parent=self.root)
					self.show()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


	def delete(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()
		try:
			if self.var_s_code.get()=="":
				messagebox.showerror("Error","Student Code must be required",parent=self.root)
			else:
				cur.execute("SELECT * FROM student where s_code=?",(self.var_s_code.get(),))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid Student code",parent=self.root)
				else:
					op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
					if op==True:
						cur.execute("delete from student where s_code=?",(self.var_s_code.get(),))
						con.commit()
						messagebox.showinfo("Success","Student deleted Succussfully",parent=self.root)
						self.clear()
				con.close()				
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)	

	

	def clear(self):
		self.var_s_code.set("")
		self.var_s_name.set("")
		self.txt_s_address.delete('1.0',END)
		self.var_s_user.set("")
		self.var_s_password.set("")
		self.var_s_gender.set("Select")		
		self.var_searchtxt.set("")		
		self.var_searchby.set("Select")		
		self.var_s_serial_no.set("")	
		self.show()

	def search(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			if self.var_searchby.get()=="Select":
				messagebox.showerror("Error","Seclect search by option",parent=self.root)
			elif self.var_searchtxt.get()=="":
				messagebox.showerror("Error","Search input is required",parent=self.root)
			else:
				cur.execute("SELECT * FROM student where "+self.var_searchby.get()+" Like '%"+self.var_searchtxt.get()+"%'")
				rows=cur.fetchall()
				if len(rows)!=0:
					self.StudentTable.delete(*self.StudentTable.get_children())
					for row in rows:
						self.StudentTable.insert('',END,values=row)
				else :
					messagebox.showerror("Error","No record found!!!",parent=self.root)
				con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)		

	def next(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			if self.var_s_serial_no.get()>=0:
				cur.execute("SELECT * FROM student where s_serial_no=?",(self.var_s_serial_no.get()+1,))
				row=cur.fetchone()
				if len(row)!=0:
					self.var_s_code.set(row[0])
					self.var_s_name.set(row[1])
					self.txt_s_address.delete('1.0',END)
					self.txt_s_address.insert(END,row[2])
					self.var_s_user.set(row[3])
					self.var_s_password.set(row[4])
					self.var_s_gender.set(row[5])			
					self.var_s_serial_no.set(row[6])	
				else :
					messagebox.showerror("Error","No record found!!!",parent=self.root)
				con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)			


if __name__=="__main__":
	root=Tk()
	obj=studentClass(root)
	root.mainloop()		