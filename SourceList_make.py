import sys


'''	
This is hard coded for the region files built by CARTA having drawn square regions.

Two source files are produced: sources_h and sources.
	The _h file is built more human-friendly, while the plain sources file is built
	for coding accessibility. _h will include region names, but will not produce 
	nicely if there are commas included in the name (as commas are used to split 
	the file)
	
	.sources_h has format 'RegionName: [RA Dec]'
	.sources has format 'RA, Dec'
'''

RegionsFile = sys.argv[1]

with open(RegionsFile) as file:
	region_list = []
	skipfirstline = file.readline()
	for line in file:
		region_list.append(line)

# Creating source list files
sourcefile_h = open(RegionsFile + ".sources_h.txt" , "w") 
sourcefile = open(RegionsFile + ".sources.txt" , "w") 

# Retrieving RA, Dec and region names
count = 0

sourcefile_h.write("Region" + "\t" + "\t" + " RA" + "\t" + "\t" + " Dec" + "\t" + "\t" + "Region Shape" + "\t" + "Notes" + "\n")

for entry in region_list:
	count = count + 1
	each = entry.split(',')
	region_h = []
	region = []

	# Removing leading 0s and reformatting declination
	firstdec = ''
	leading0 = True
	each[1] = each[1].split('.')

	if (each[1][0][1] == '-'):
		firstdec = each[1][0][1]

	for i in range(2,len(each[1][0])-1):

		if (each[1][0][i] == '0' and leading0 == True):
			firstdec = firstdec

		elif (each[1][0][i] != '0' and leading0 == True):
			firstdec = firstdec + each[1][0][i]
			leading0 = False

		else:
			firstdec = firstdec + each[1][0][i]

	firstdec = firstdec + each[1][0][-1]

	dec = " " + firstdec + ':' + each[1][1] + ':' + each[1][2] + "." + each[1][3]

	# Checking for and adding notes/specified names of the regions
	nametest = []

	try:
		nametest = each[16]
		name = each[-3][8:-1]

	except:
		name = '\t'

	# Adjusting for differently shaped regions and removing extra char from RA value

	if each[0][0] == 'c' :
		each[0] = each[0][8:]
		shape = "Rectangle"

	elif each[0][0] == 'e':
		each[0] = each[0][6:]
		shape = "Ellipse"

	region_h.append(["Region " + str(count) + ": \t", each[0][3:], '\t', dec, "\t" + shape + "\t" + name])
	region.append([each[0][4:], "\t", dec[:-1]])

	# Writing to source lists
		# Note 'i' is the list of objects relating to each region (along with 
		# formatting, should it apply) e.g. [name, RA, Dec] and 'j' is each of
		# those components
	
	for i in region_h:
			for j in i:
				sourcefile_h.write(j)
			sourcefile_h.write('\n')

	for i in region:
		for j in i:
			sourcefile.write(j)
		sourcefile.write('\n')
		
sourcefile.close()
sourcefile_h.close()

		


