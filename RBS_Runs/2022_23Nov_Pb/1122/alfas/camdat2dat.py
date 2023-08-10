import sys

# Open the file
f_input = sys.argv[-1]+".dat"
f_output = sys.argv[-1]+"_sort.dat"

fi = open(f_input,"r")
fo = open(f_output,"w")

i=0
j=-1
array = []
data = []
for line in fi:
   
# Read the first line
	array.append([int(x) for x in line.split()])
	for val in array[i]:
		if (j>0): fo.write("%i %i \n" % (j,val))
#		data[j]= val
		j= j+1
#		print (data[j])
#	print (array[i])
	i = i+1

fo.close()

# Read lines until you get the argument "$Angles"


# Write the data in an output file for further representation and/or analysis