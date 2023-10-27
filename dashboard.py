from tkinter import*
from PIL import Image,ImageTk
from student import studentClass
from testdetails import testdetailsClass
from testresult import testresultClass
from datetime import date
from datetime import datetime

class IMS:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1350x700+0+0")
		self.root.title("Quizhack System | Developed by Mahi")
		self.root.config(bg="white")

		#===title===
		title=Label(self.root,text="Quizhack System",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1,height=70)

		#===btn_logout===
		btn_logout=Button(self.root,text="Logout",command=self.logout_time,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=5,height=60,width=150)

		#===clock===
		self.lbl_clock=Label(self.root,text="Wlecome to Quizhack System\t\t Date(YYYY-MM-DD): "+str(date.today())+"\t\t Time: HH:MM:SS "+str(datetime.now().strftime("%H:%M:%S")),font=("times new roman",15),bg="#4d636d",fg="white")
		self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

		#===Left Menu===
		LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
		LeftMenu.place(x=0,y=102,width=200,height=575)		

		lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
		btn_student=Button(LeftMenu,text="Student",command=self.student,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
		btn_test=Button(LeftMenu,text="Test",command=self.testdetails,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
		btn_result=Button(LeftMenu,text="Result",command=self.testresult,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
		btn_exit=Button(LeftMenu,text="Exit",command=self.logout_time,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

		#===content===	
		#self.lbl_student=Label(self.root,text="Student",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
		#self.lbl_student.place(x=300,y=120,height=150,width=300)

		btn_student_big=Button(self.root,text="Student",command=self.student,bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))		
		btn_student_big.place(x=300,y=120,height=150,width=300)

		#self.lbl_test=Label(self.root,text="test",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
		#self.lbl_test.place(x=650,y=120,height=150,width=300)	

		btn_test_big=Button(self.root,text="test",command=self.testdetails,bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
		btn_test_big.place(x=650,y=120,height=150,width=300)			

		#self.lbl_result=Label(self.root,text="Result",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
		#self.lbl_result.place(x=1000,y=120,height=150,width=300)

		btn_result_big=Button(self.root,text="Result",command=self.testresult,bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
		btn_result_big.place(x=1000,y=120,height=150,width=300)

		#===footer===
		lbl_footer=Label(self.root,text="Quizhack System | Developed by Mahi\nFor any Technical Issue Contact: 97XXXXXXXX",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

		#===============================================================================

	def student(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=studentClass(self.new_win)

	def testdetails(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=testdetailsClass(self.new_win)	

	def testresult(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=testresultClass(self.new_win)	

	def logout_time(self):
		exit()			

if __name__=="__main__":
	root=Tk()
	obj=IMS(root)
	root.mainloop()
