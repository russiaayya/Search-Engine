import re
import os
import codecs


#create new file
def create_file(filename):
	if not os.path.isfile(filename):
		write_to_file(filename, '')


# create new directory
def create_dir(dir):
	if not os.path.exists(dir):
		print "creating dir", dir
		os.makedirs(dir)


# write data to file
def write_to_file(filepath, content):
	with open(filepath, 'w') as f:
		f.write(content)


#renaming and moving file
def renaming_file(filename,dir):
	#id_dict = {}
	lines_list = []
	lines_list = open(filename).read().splitlines()
	# for line in lines_list:
	name = lines_list[0].split('https://en.wikipedia.org/wiki/')[1]
	new_name = dir+name+".txt"
	print "renaming ",filename, new_name
	os.rename(filename,new_name)



def write_bm25Dic_to_file(filepath, content):
    rank = 1
    file = open(filepath,"w")
    for item in content:
        file.write(item)
        rank +=1
        file.write("\n")

    file.close()


