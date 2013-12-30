from os import listdir
from os import mkdir
from shutil import copy


files = listdir("original_files")

alphabet = map(chr, range(97,123))
for letter in alphabet:
	mkdir(letter)		

for file in files:
	file_name = "original_files/" + file
	first_letter = file[0]
	copy(file_name,first_letter) 










