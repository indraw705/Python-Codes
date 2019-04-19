import os

os.chdir("/home/inarvekar/Desktop/pYcODES/FilesProgs")

for f in os.listdir():
	file_name, fileExt = os.path.splitext(f)
	# print(file_name, fileExt)
	names, spaces = file_name.split("-")
	# print(names[2:])
	extension, num = fileExt.split()
	# print(num)
	new_name = ("{}_{}{}".format(num,names[2:].strip(),extension))

	os.rename(f,new_name)