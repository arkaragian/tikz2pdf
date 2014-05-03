import sys
import os
import argparse

#===================
# Function Definitions
#===================

#Prepare the input file for standalone compilation
#This is done with a different filename
def conditionTex(filename):
	inFile = open(filename, 'r')
	tempName = "temp-"+filename
	
	outFile = open(tempName,'w')
	
	#Write a new line in case the original file starts with a comment
	outFile.write('\n')
	outFile.write('\\documentclass{standalone}\n')
	outFile.write('\\usepackage{tikz}\n')
	outFile.write('\\begin{document}\n')
	outFile.write('\\begin{tikzpicture}\n')
	for line in inFile:
		outFile.write(line)
		
	#Write a new line in case the original file ends with a comment
	outFile.write('\n')
	outFile.write('\\end{tikzpicture}\n')
	outFile.write('\\end{document}\n')
	
	inFile.close()
	outFile.close()
	
def clean_temp_files(filename):
	no_extension = os.path.splitext(file)
	os.remove("temp-"+no_extension[0]+".aux")
	os.remove("temp-"+no_extension[0]+".log")
	os.remove("temp-"+no_extension[0]+".tex")



#===================
# Program
#===================

parser = argparse.ArgumentParser(description='tikz2pdf: Convert a tikz source to pdf')
#A positional argument(This should be supplied for the program to run)
parser.add_argument('file', help='Filename to process')
inputs  = parser.parse_args()
#print(inputs.file)

#Store the input file in a variable
file = inputs.file 
conditionTex(file)

#This command will be used. It should be in the system path
command = "pdflatex -halt-on-error -interaction=nonstopmode "+"temp-"+file
exit_status = os.system(command)

#If the comannd have completed successfully
if exit_status != 0:
	print('Compilation of '+file+' failed')
	clean_temp_files(file)
	sys.exit(1)
else:
	print('Compilation of '+file+' completed')
	no_extension = os.path.splitext(file);
	try:
		os.rename("temp-"+no_extension[0]+".pdf",no_extension[0]+".pdf")
	except OSError as e: #This will be raised on Windows environments
		os.remove(no_extension[0]+".pdf")
		os.rename("temp-"+no_extension[0]+".pdf",no_extension[0]+".pdf")
	
	clean_temp_files(file)
	sys.exit(0)
