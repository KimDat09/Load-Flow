import sqlite3
# import openpyxl
# import os
# import pandas as pd 

def Admin(name):
	#tạo bảng và các dữ liệu 
	conn=sqlite3.connect(name)
	cursor=conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS "BUS"(NO,NAME,kV,Code)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  LINE(NO,FROMBUS,TOBUS,CID,Rpu,Xpu,Gpu,Bpu,Length)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  GEN(NO,CID,Vsched,P,Q,Qmax,Qmin,Xd)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  LOAD(NO,CID,P,Q)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  OPTION(NAMEOPT,VALUE)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  BRANCH_RESULT(NO,FROMBUS,TOBUS,CID,P1,Q1,I1,P2,Q2,I2)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  BUS_RESULT(NO,MAG,ANG)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  X2TRANSFORMER(NO,FROMBUS,TOBUS,Rpu,Xpu,Gpu,Bpu,Winding1,Winding2,S_MVA)')

	cursor.execute('CREATE TABLE IF NOT EXISTS  SHUNT(NO,BUS,ID,Q_nom,U_nom)')








	# cursor.execute('CREATE TABLE IF NOT EXISTS  "Đường_dây"(NO,Bắt_đầu,Kết_thúc,FLAG,FLAG3,LENGTH,R_Ohm,X_Ohm,B_microSiemens,RATE_A)')

	conn.commit()
	conn.close()
	print("case created")

if __name__ == '__main__':
	name='5nut.db'
	Admin(name)



