import math
import sys
import csv
################################
# Helper functions 
def EntroCalc(x1, x2):
	Total = x1 + x2
	if x1 == Total or x2 == Total:
		return 0
	else:
		p = float(x1)/float(Total)
		entro = -p*math.log(p, 2)-(1-p)*math.log((1-p),2)
		return entro

# calculate the entropy of each node and information gain of the whole brunch
def IGCalc(DT):
	Top = DT[0]
	Branch1 = DT[1]
	Branch2 = DT[2]
	topEntro = EntroCalc(Top[0], Top[1])
	B1Entro = EntroCalc(Branch1[0], Branch1[1])
	B2Entro = EntroCalc(Branch2[0], Branch2[1])
	p1 = math.fsum(Branch1)/math.fsum(Top)
	p2 = math.fsum(Branch2)/math.fsum(Top)
	IG = topEntro - p1* B1Entro-p2*B2Entro
	return IG

###################################
# csv file read and write
# read csv file from input file 
def csvReader(input):
	csvfile = open(input)
	data = csv.reader(csvfile)
	listRow = [ ]
	listCol = [ ]
	for row in data:
		listRow.append(row)
	for i in range(len(listRow[0])):
		col = [ ]
		for row in listRow:
			col.append(row[i])
		listCol.append(col)
	return listCol
##################################
# count the number for each result
def countResult(col, label1, label2):
	count1 = 0
	count2 = 0
	for item in col[1:]:
		if item == label1:
			count1 += 1
		else:
			count2 += 1
	return [count1, count2]
	
# Count the label of each attribute and output
def labelCounter(attribute):
# build a dictionary that return the result: [yes, no]
	label = [ ]
	for item in attribute[1:]:
		if item not in label:
			label.append(item)
	return label

# Output the divided results for two labels
# return result {yes:[], no:[]}
def separate(attrCol, ResultCol):
	[attrlab1, attrlab2] = labelCounter(attrCol)
	list1 = [ResultCol[0]]
	list2 = [ResultCol[0]]
	for i in range(1,len(attrCol)):
		if attrCol[i] ==attrlab1:
			list1.append(ResultCol[i])
		else:
			list2.append(ResultCol[i])
	result = {attrlab1:list1, attrlab2:list2}
	return result

# Once find the attribute of the largest information gain, make a new list divided by the label
# Return a dict {attr1:[list1], attr2:[list2]}
def makeNewDatafile(attrCol, listCol):
	[attrlab1, attrlab2] = labelCounter(attrCol)
	newFile = dict()
	newFile[attrlab1] = []
	newFile[attrlab2] = []
	for row in listCol:
		result = separate(attrCol, row)
		newFile[attrlab1].append(result[attrlab1])
		newFile[attrlab2].append(result[attrlab2])
	return newFile
#######################
def majorityVote(Col):
	labelSet = labelCounter(Col)
	if len(labelSet) == 1: return labelSet
	else:
		result = countResult(Col, labelSet[0], labelSet[1])
		if result[0] > result[1]:
			return [labelSet[0]]
		else:
			return [labelSet[1]]
# reach to a tie ? 
##################################
# output the decision tree 
def dtPrint(listCol, ylabel, depth, preAttr, label):
	result = countResult(listCol[-1], ylabel[0], ylabel[1])
	if depth == 0:
		print([str(result[0])+" " + ylabel[1] + "/" + str(result[1]) + ylabel[1]])
	else:
		print("|"*depth + preAttr + "=" + label , [str(result[0])+" " + ylabel[1] + "/" + str(result[1]) + ylabel[1]])
############################
# Write a stump file to print the result of each stump and output two subcsvfile
def stump(listCol, ylabel, depth=0, depthLimit, preAttr=" ", label=" "):
	dtPrint(listCol, ylabel, depth, preAttr, label)
	if depth >= 3:
		return majorityVote(listCol[-1])
	else:
		top = countResult(listCol[-1], ylabel[0], ylabel[1])
	# find the attribute of the largest information gain	
		mIG = 0
		mai = 0
		mls = [ ]
		for i in range(len(listCol)-1):
	# the attribute divided which equal to one should not be divided again
			if len(labelCounter(listCol[i])) == 1:
				continue
			else:
				result = separate(listCol[i], listCol[-1])
				Branch = [ ]
				labSet = [ ]
				for label in result:
					branch = countResult(result[label], ylabel[0], ylabel[1])
					Branch.append(branch)
					labSet.append(label)
				DT = [top]+Branch
				IG = IGCalc(DT)
				if IG > mIG:
					mIG = IG
					mai = i
					mls = labSet
	# Calculate the Attribute of the most information gain 	
		if mIG <= 0:
			return majorityVote(listCol[-1])
		else:
			Newfile = makeNewDatafile(listCol[mai], listCol)
	# return a list like [Attribute, [Yes, stump], [No, stump]]
		return [listCol[mai][0], [mls[0], stump(Newfile[mls[0]], ylabel, depth+1, depthLimit, listCol[mai][0], mls[0])], 
				[mls[1], stump(Newfile[mls[1]], ylabel, depth+1, depthLimit, listCol[mai][0], mls[1])]]
####################################################
# determine results
def evaluate(DT, row)
# make output file
def outPut(DT, train, test, trainOUT, testOUT, metrics):





####################################################
# main function
if __name__ == '__main__':
	train = sys.argv[1]
	test = sys.argv[2]
	maxDepth = sys.argv[3]
	trainOUT = sys.argv[4]
	testOUT = sys.argv[5]
	metrics = sys.argv[6]
	# make decision tree
	listCol = csvReader(train)
	yLabel = labelCounter(listCol[-1])
	DT = stump(listCol, yLabel, 0, maxDepth)
	# output all the result
	outPut(DT, train, test, trainOUT, testOUT, metrics)




	














