import re
import os
import codecs


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


# write data to file
def write_to_file(filepath, content):
	with open(filepath, 'w') as f:
		f.write(content)

# write data from dictionary to file
def write_dic_to_file(filename,content):
	with codecs.open(filename,'w',encoding= 'utf-8') as f:
		for key,value in content.iteritems():
			f.write(str(key)+' '+' '.join(value)+'\n')



def write_index_to_file(filename, content):
	lst = []

	for key, value in content.iteritems():
		tstr = " "
		for vk, vv in value.iteritems():
			tstr = tstr + "("+ vk + "," + str(vv) + ")"
		poststr = tstr

		poststr = key + " -> "+ poststr

		lst.append(poststr)

	write_list_to_file(filename, lst)


# write data extracting from list to file 
def write_list_to_file(filename, lst):
	with codecs.open(filename,'w',encoding= 'utf-8') as f:
		for l in lst:
			f.write(str(l) + "\n")



def write_file_tolist(filename):
    data = []
    with open(filename, 'rt') as lfile:
        for line in lfile:
			data.append(line.replace('\n', ''))
    return data



#create new file
def create_file(filename):
	if not os.path.isfile(filename):
		write_to_file(filename, '')


# create new directory
def create_dir(dir):
	if not os.path.exists(dir):
		print "creating dir", dir
		os.makedirs(dir)





