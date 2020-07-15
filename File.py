def Read_Diary(read_file_path):
	read_file_content=''
	try:
		with open(read_file_path,'r'):
			return(read_file_content)
	except:
		return('Error')


def Save_Diary(Content,file_path):
	with open(file_path,"a") as f:
		f.write("\n")
		f.write(Content)