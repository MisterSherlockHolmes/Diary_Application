def Read_Diary(read_file_path):
	read_file_content=''
	try:
		with open(read_file_path,'r') as read_file_content:
			return(read_file_content)
	except:
		return('Error')


def Save_Diary(Content,file_path):
	with open(file_path,"w") as f:
		f.write(Content)
