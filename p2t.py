def pdffolder2txtfolder(input_folder,output_folder):
	import subprocess, os
	for input_file in os.listdir(input_folder):
		if input_file.endswith(".pdf"):

			output_file= input_file.replace(".pdf",".txt")
			input_dir=input_folder+"/"+input_file
			#print input_dir
			output_dir=output_folder+"/"+output_file
			#print output_dir
			task=['pdf2txt.py','-o',output_dir,input_dir]
			#print task

			subprocess.check_call(task)
	print("Done !")


input_folder="/Users/macbook/Documents/RA/Training_set_false1_pdf"
output_folder="/Users/macbook/Documents/RA/Training_set_false1_txt"
pdffolder2txtfolder(input_folder,output_folder)
