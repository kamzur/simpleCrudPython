#!/usr/bin/python

import MySQLdb

class DatabaseMhs:
	
	host = "localhost"
	user = "root"
	pasw = ""
	dbnm = "test"	
	
	nim = ""
	nama = ""
	email = ""
	jurusan = ""
		
		
	def do_connect(self):
		# open database 
		self.db = MySQLdb.connect(self.host,self.user,self.pasw,self.dbnm)
		# prepare db using cursor
		self.csr = self.db.cursor()
		
	def set_mhs(self,nim,nama,email,jurusan):
		self.nim = nim
		self.nama = nama
		self.email = email
		self.jurusan = jurusan
		self.insert_mhs()
		
	def insert_mhs(self):
		
		self.do_connect()
		
		sql = "INSERT INTO mhs VALUES('%s','%s','%s','%s')" % \
		(self.nim,self.nama,self.email,self.jurusan)
		
		try:
			self.csr.execute(sql)
			self.db.commit()
		except:
			# rollback in case there is any error
			self.db.rollback()
		
		self.close_db()
			
	def close_db(self):
		# disconnected
		self.db.close()

