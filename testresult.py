from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlanydb

class testresultClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1100x500+220+130")
		self.root.title("Quizhack System | Developed by Mahi")
		self.root.config(bg="white")
		self.root.focus_force()

		self.var_q_code_q=StringVar()
		self.var_q_details=StringVar()
		self.var_qa_ans=StringVar()
		self.var_s_code=StringVar()
		self.var_qo_options=StringVar()
		

		#===========================Title=========================================
		title=Label(self.root,text="Student Testing Result",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=50,y=10,width=1000)

		#===========================Question Details===============================
		lbl_s_code=Label(self.root,text="Student Code",font=("goudy old style",15),bg="white").place(x=50,y=60)
				
		txt_s_code=Entry(self.root,textvariable=self.var_s_code,font=("goudy old style",15),bg="white").place(x=180,y=60,width=200)
		#================Button===========================================
		btn_next=Button(self.root,text="Next",command=self.show,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=400,y=60,width=150,height=30)
				
		#==============Question options=======================
		testresult_frame=Frame(self.root,bd=3,relief=RIDGE)
		testresult_frame.place(x=0,y=100,relwidth=1,height=400)
		scrolly=Scrollbar(testresult_frame,orient=VERTICAL)
		scrollx=Scrollbar(testresult_frame,orient=HORIZONTAL)

		self.TestresultTable=ttk.Treeview(testresult_frame,columns=("q_code","q_details","qo_options","qa_ans"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM,fill=X)
		scrolly.pack(side=RIGHT,fill=Y)
		scrollx.config(command=self.TestresultTable.xview)
		scrolly.config(command=self.TestresultTable.yview)

		self.TestresultTable.heading("q_code",text="Code")
		self.TestresultTable.heading("q_details",text="Question")
		self.TestresultTable.heading("qo_options",text="Selected Option")
		self.TestresultTable.heading("qa_ans",text="Correct Option")
		self.TestresultTable["show"]="headings"

		self.TestresultTable.column("q_code",width=90)
		self.TestresultTable.column("q_details",width=190)
		self.TestresultTable.column("qo_options",width=20)
		self.TestresultTable.column("qa_ans",width=20)
		self.TestresultTable.pack(fill=BOTH,expand=1)
		self.TestresultTable.bind("<ButtonRelease-1>",self.get_data)

		#self.show()

	def show(self):
		con=sqlanydb.connect(DSN="quizhack",UID="admin",PWD="Pintu@355")
		cur = con.cursor()		
		try:
			if len(str(self.var_q_code_q.get()))>=0:
				cur.execute("SELECT sans.q_code , ques.q_details , sans.qo_option , qans.qa_ans FROM m_question ques , question_ans qans , student_ans  sans where ques.q_code = sans.q_code and qans.q_code = sans.q_code and sans.s_code=?",(self.var_s_code.get(),))
				rows=cur.fetchall()
				self.TestresultTable.delete(*self.TestresultTable.get_children())
				for row in rows:
					self.TestresultTable.insert('',END,values=row)
				con.close()	
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

	def get_data(self,ev):
		f=self.TestresultTable.focus()
		content=(self.TestresultTable.item(f))
		row=content['values']
		#print(row)
		self.var_q_code_q.set(row[0])
		self.var_q_details.set(row[1])
		self.var_qo_options.set(row[2])
		self.var_qa_ans.set(row[3])
		

if __name__=="__main__":
	root=Tk()
	obj=testresultClass(root)
	root.mainloop()		