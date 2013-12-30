from os import listdir
from os import mkdir
from os import remove
from os.path import exists
from shutil import move
from shutil import copy
from os import chdir
from os import getcwd

files = listdir("original_files")

alphabet = map(chr, range(97,123))
for letter in alphabet:
	mkdir(letter)		

for file in files:
	file_name = "original_files/" + file
	first_letter = file[0]
	copy(file_name,first_letter) 










	# how to make first_letter refer to the directory above?

	#if exists(first_letter) == False:
		#mkdir(first_letter)
		# move(file, first_letter)
	# else:
		# copy2(file, first_letter)
		# chdir("files") 