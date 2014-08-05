#!/usr/bin/python

from Tkinter import *
from database_mhs import *
import tkMessageBox

class GuiMhs:
	
	nim = ""
	nama = ""
	email = ""
	jurusan = ""
	notif = ""
	
	
	def __init__(self):
		self.root = Tk()
		self.nim = StringVar()
		self.nama = StringVar()
		self.email = StringVar()
		self.jurusan = StringVar()
		self.notif = StringVar()
		
		self.root.title("MAHASISWA")
		
		self.db = DatabaseMhs()
		self.initGui()
		self.root.mainloop()
		
	def initGui(self):
		#self.frm()
		self.txt_input()
		self.btn_insert()
		self.lbl_input()
		
	def txt_input(self):
		# text input untuk nim pada frame atas
		self.txt_nim = Entry(self.root, bd=1, textvariable=self.nim)
		self.txt_nim.grid(row=0, column=1,sticky=E)
		
		# text input untuk nama pada frame tengah 1
		self.txt_nama = Entry(self.root, bd=1, textvariable=self.nama)
		self.txt_nama.grid(row=1, column=1,sticky=E)
		
		# text input untuk email pada frame tengah 2
		self.txt_email = Entry(self.root, bd=1, textvariable=self.email)
		self.txt_email.grid(row=2, column=1,sticky=E)
		
		# text input untuk jurusan pada frame bawah
		self.txt_jur = Entry(self.root, bd=1, textvariable=self.jurusan)
		self.txt_jur.grid(row=3, column=1,sticky=E)
		
	def lbl_input(self):
		# label nim pada frame atas
		lbl_nim = Label(self.root, text="Nim ")
		lbl_nim.grid(row=0, column=0, sticky=W)
		
		# label nama pada frame tengah 1
		lbl_nama = Label(self.root, text="Nama ")
		lbl_nama.grid(row=1, column=0, sticky=W)
		
		# label email pada frame tengah 2
		lbl_email = Label(self.root, text="Email")
		lbl_email.grid(row=2, column=0, sticky=W)
		
		
		# label jurusan pada frame bawah
		lbl_jur = Label(self.root, text="Jurusan")
		lbl_jur.grid(row=3, column=0, sticky=W)
		
		# label pembatas
		lbl_bts = Label(self.root, text="")
		lbl_bts.grid(row=4, column=0, columnspan=1)
		
	def btn_insert(self):
		# buat tombol insert di frame btn
		self.btn_insert = Button(self.root, text="Tambah")
		self.btn_insert.bind("<Button-1>",self.get_data_entry)
		self.btn_insert.grid(row=5, column=1, ipadx=21, sticky=NW)

		# buat tombol cancel di frame btn
		self.btn_cancel = Button(self.root, text="Clear")
		self.btn_cancel.bind("<Button-1>",self.clear_entry)
		self.btn_cancel.grid(row=5, column=0,ipadx=20, sticky=NE)
		
		
	# method ini digunakan untuk 
	# mengambil data entry.
	# yang nantinya akan ditampung dulu 
	# ke dalam variabel (properti)
	# ke kelas database mhs
	def get_data_entry(self, event=None):
		if self.check_val() != False:
			nim = self.nim.get()
			nama = self.nama.get()
			email = self.email.get()
			jurusan = self.jurusan.get()
			self.db.set_mhs(nim,nama,email,jurusan)
			self.clear_entry()
		
		
	def clear_entry(self, event=None):
		self.txt_nim.delete(0, END)
		self.txt_nama.delete(0, END)
		self.txt_email.delete(0, END)
		self.txt_jur.delete(0, END)
		
	# buat ngecek ke kosongan data	
	def check_val(self):
		if self.nim.get() == "" or len(self.nim.get()) < 2:
			self.window_notif("nim harus di isi\nminimal 3 karakter")
			return False
		elif self.nama.get() == "" or len(self.nama.get()) < 2:
			self.window_notif("nama harus di isi\nminimal 3 karakter")
			return False
		elif self.email.get() == "" or len(self.email.get()) < 2:
			self.window_notif("email tak boleh kosong")
			return False
		elif self.jurusan.get() == "" or len(self.jurusan.get()) < 2:
			self.window_notif("jurusan harus di isi")
			return False
		else:
			return True
		
	def window_notif(self,str):
		self.top = self.root
		self.top = Toplevel()
		str = self.notif.set(str)
		font = 'arial 18 bold'
		lbl_notif = Label(self.top, textvariable=self.notif,justify=LEFT, font=font, fg="red", bg='white')
		lbl_notif.pack()
		self.top.title("perhatian !")
		self.top.resizable(0,0)
		self.top.mainloop()	