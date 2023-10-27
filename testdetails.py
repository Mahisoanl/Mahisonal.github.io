from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlanydb

class testdetailsClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1100x500+220+130")
		self.root.title("Quizhack System | Developed by Mahi")
		self.root.config(bg="white")
		self.root.focus_force()

		self.var_q_code_q=StringVar()
		self.var_q_code_q.set('Q001')
		self.var_q_details=StringVar()
		self.var_q_type=StringVar()
		self.var_q_serial_no=IntVar()
		self.var_q_code_op=StringVar()

		self.var_qo_options=StringVar()
		self.var_qo_details=StringVar()

		self.var_q_ans_code=StringVar()
		
		self.var_s_code=StringVar()
		self.var_s_code.set('P001')
		self.var_q_message=StringVar()

		self.var_q_student_name=StringVar()
		self.var_q_student_list=StringVar()
		#===========================Title=========================================
		title=Label(self.root,text="Student Testing Details",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=50,y=10,width=1000)

		#===========================Question Details===============================
		lbl_q_code_q=Label(self.root,text="Code",font=("goudy old style",15),bg="white").place(x=50,y=60)
		lbl_s_code=Label(self.root,text="Student",font=("goudy old style",15),bg="white").place(x=750,y=60)
		lbl_q_details=Label(self.root,text="Question",font=("goudy old style",15),bg="white").place(x=50,y=100)
		lbl_q_serial_no=Label(self.root,text="Serial No.",font=("goudy old style",15),bg="white").place(x=850,y=100)
		lbl_q_ans_code=Label(self.root,text="Answer",font=("goudy old style",15),bg="white").place(x=50,y=420)
		#cmb_q_student_name=ttk.Combobox(self.root,textvariable=self.var_q_student_name,values=(self.var_q_student_list),state='readonly',justify=LEFT,font=("goudy old style",15))
		#cmb_q_student_name.place(x=850,y=150,width=220)
		#cmb_q_student_name.current(0)
		self.show_student()

		txt_q_code_q=Entry(self.root,textvariable=self.var_q_code_q,font=("goudy old style",15),bg="white").place(x=150,y=60,width=120)
		txt_s_code=Entry(self.root,textvariable=self.var_s_code,font=("goudy old style",15),bg="white").place(x=850,y=60,width=2)
		self.txt_q_details=Text(self.root,font=("goudy old style",15),bg="white")
		self.txt_q_details.place(x=150,y=110,width=650,height=80)
		txt_q_serial_no=Entry(self.root,textvariable=self.var_q_serial_no,font=("goudy old style",15),bg="white").place(x=950,y=100,width=100)
		txt_q_ans_code=Entry(self.root,textvariable=self.var_q_ans_code,font=("goudy old style",15),bg="white").place(x=150,y=420,width=120)
		txt_q_message=Entry(self.root,textvariable=self.var_q_message,font=("goudy old style",15),bg="white").place(x=150,y=460,width=300)

		#================Button===========================================
		btn_update=Button(self.root,text="Save",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=420,width=150,height=30)
		btn_next=Button(self.root,text="Next",command=self.next,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=520,y=420,width=150,height=30)
		btn_previous=Button(self.root,text="Previous",command=self.previous,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=740,y=420,width=150,height=30)
		
		#==============Question options=======================
		question_frame=Frame(self.root,bd=3,relief=RIDGE)
		question_frame.place(x=0,y=220,relwidth=1,height=180)
		#scrolly=Scrollbar(question_frame,orient=VERTICAL)
		#scrollx=Scrollbar(question_frame,orient=HORIZONTAL)

		#self.QuestionTable=ttk.Treeview(question_frame,columns=("qo_options","qo_details"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		self.QuestionTable=ttk.Treeview(question_frame,columns=("qo_options","qo_details"))
		#scrollx.pack(side=BOTTOM,fill=X)
		#scrolly.pack(side=RIGHT,fill=Y)
		#scrollx.config(command=self.QuestionTable.xview)
		#scrolly.config(command=self.QuestionTable.yview)

		self.QuestionTable.heading("qo_options",text="Option")
		self.QuestionTable.heading("qo_details",text="Details")
		self.QuestionTable["show"]="headings"

		self.QuestionTable.column("qo_options",width=10)
		self.QuestionTable.column("qo_details",width=190)
		self.QuestionTable.pack(fill=BOTH,expand=1)
		self.QuestionTable.bind("<ButtonRelease-1>",self.get_data)

		self.show()

	def show(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()		
		try:
			if len(str(self.var_q_code_q.get()))>=0:
				cur.execute("SELECT * FROM m_question where q_code=?",(self.var_q_code_q.get(),))
				row=cur.fetchone()
				if len(row)!=0:
					self.var_q_code_q.set(row[0])
					self.txt_q_details.delete('1.0',END)
					self.txt_q_details.insert(END,row[1])
					self.var_q_type.set(row[2])
					self.var_q_serial_no.set(row[3])
				else :
					messagebox.showerror("Error","No record found!!!",parent=self.root)

			cur.execute("SELECT qo_options , qo_details  FROM question_options  where q_code=? order by qo_options",(self.var_q_code_q.get(),))
			rows=cur.fetchall()
			self.QuestionTable.delete(*self.QuestionTable.get_children())
			for row in rows:
				self.QuestionTable.insert('',END,values=row)
			con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

	def get_data(self,ev):
		f=self.QuestionTable.focus()
		content=(self.QuestionTable.item(f))
		row=content['values']
		#print(row)
		#self.var_s_code.set(row[0])
		self.var_qo_options.set(row[0])
		self.var_qo_details.set(row[1])
		
		

	def next(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			if self.var_q_serial_no.get()>=0:
				cur.execute("SELECT * FROM m_question where q_serial_no=?",(self.var_q_serial_no.get()+1,))
				row=cur.fetchone()
				if len(row)!=0:
					self.var_q_code_q.set(row[0])
					self.txt_q_details.delete('1.0',END)
					self.txt_q_details.insert(END,row[1])
					self.var_q_type.set(row[2])
					self.var_q_serial_no.set(row[3])
				else :
					messagebox.showerror("Error","No record found!!!",parent=self.root)
				
				cur.execute("SELECT qo_options , qo_details  FROM question_options  where q_code=? order by qo_options",(self.var_q_code_q.get(),))
				rows=cur.fetchall()
				self.QuestionTable.delete(*self.QuestionTable.get_children())
				for row in rows:
					self.QuestionTable.insert('',END,values=row)
				self.var_q_ans_code.set("")
				self.var_q_message.set("")
				con.close()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)			
	
	def previous(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			if self.var_q_serial_no.get()-1>=1:
				cur.execute("SELECT * FROM m_question where q_serial_no=?",(self.var_q_serial_no.get()-1,))
				row=cur.fetchone()
				if len(row)!=0:
					self.var_q_code_q.set(row[0])
					self.txt_q_details.delete('1.0',END)
					self.txt_q_details.insert(END,row[1])
					self.var_q_type.set(row[2])
					self.var_q_serial_no.set(row[3])
				else :
					messagebox.showerror("Error","No record found!!!",parent=self.root)
				
				cur.execute("SELECT qo_options , qo_details  FROM question_options  where q_code=? order by qo_options",(self.var_q_code_q.get(),))
				rows=cur.fetchall()
				self.QuestionTable.delete(*self.QuestionTable.get_children())
				for row in rows:
					self.QuestionTable.insert('',END,values=row)
				self.var_q_ans_code.set("")
				self.var_q_message.set("")
				con.close()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)				


	def update(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()
		try:
			s_student = self.var_q_student_name.get()
			self.var_s_code.set(s_student[:4])
			#print(s_student[:4])
			if self.var_s_code.get()=="":
				messagebox.showerror("Error","Student selection must be required",parent=self.root)
			else:
				cur.execute("SELECT count(*) FROM question_ans where q_code=?",(self.var_q_code_q.get(),))
				row=cur.fetchone()
				if len(row)!=0:
					cur.execute("SELECT qa_ans FROM question_ans where q_code=?",(self.var_q_code_q.get(),))
					row=cur.fetchone()
					if len(row)!=0:
						if self.var_q_ans_code.get() != row[0]:
							self.var_q_message.set("Correct answer is "+str(row[0]))
							cur.execute("update student_ans set qo_option=?where s_code=? and q_code=?",(
											self.var_q_ans_code.get(),
											self.var_s_code.get(),
											self.var_q_code_q.get(),											
							))
					else:
						cur.execute("insert into student_ans (s_code,q_code,qo_option) values(?,?,?)",(						
										self.var_s_code.get(),
										self.var_q_code_q.get(),
										self.var_q_ans_code.get(),
					))
						con.commit()
						con.close()
						messagebox.showinfo("Success","Data Updated Succussfully",parent=self.root)
				else:
					messagebox.showerror("Error","No record found!!!",parent=self.root)
					
				#self.show()
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

	def show_student(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()			
		try:
			
			cur.execute("SELECT s_code , s_name FROM student")
			rows=cur.fetchall()
			for row in rows:
				self.var_q_student_list = row
		#		self.StudentTable.insert('',END,values=row)
			cmb_q_student_name=ttk.Combobox(self.root,textvariable=self.var_q_student_name,values=(rows),state='readonly',justify=LEFT,font=("goudy old style",15))
			cmb_q_student_name.place(x=850,y=60,width=200)
			cmb_q_student_name.current(0)	
			con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
	

if __name__=="__main__":
	root=Tk()
	obj=testdetailsClass(root)
	root.mainloop()		