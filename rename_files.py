import os

def rename_files():
	file_list=os.listdir()
	print(file_list)
	for filename in file_list:
		os.rename(filename,filename.translate("0123456789"))


rename_files()