import sys
import csv
import numpy as np
import math
import time 
def readfile(input):
	tvs = open(input, "r+")
	file = csv.reader(tvs, delimiter="\t")
	tvsFile = []
	for row in file:
		tvsFile.append(row)
	#print (tvsFile)
	return ([[]] + tvsFile + [[]])	
# make a list contain different attributes 
def makelist(tvsFile):
	attributeList = []
	labList = []
	for row in tvsFile:
		if row == [ ]:
			continue
		if row[0] not in attributeList:
			attributeList.append(row[0])
		if row[1] not in labList:
			labList.append(row[1])
	return attributeList, labList
#######################################
# SGD Calculation
def xVector1(row, attributeList):	
	Numb = attributeList.index(row[0])
	vector = np.zeros(len(attributeList)+1)
	vector[0] = 1
	vector[1+Numb] = 1
	#arr = np.array([1]+[0]*Numb+[1]+[0]*(len(attributeList)-Numb-1))
	#print(arr.shape)
	return vector
def xVector2(rows, attributeList):
	N = len(attributeList)
	vector = np.zeros(3*N+3)
	vector[0] = 1
	if rows[0] == []:
		vector[1] = 1
		numb2, numb3 = attributeList.index(rows[1][0]), attributeList.index(rows[2][0])
		vector[2+N+numb2], vector[2+2*N+numb3] = 1, 1
	elif rows[2] == []:
		vector[-1] = 1
		numb1, numb2 = attributeList.index(rows[0][0]), attributeList.index(rows[1][0])
		vector[2+numb1], vector[2+N+numb2] = 1, 1
	else :
		numb1, numb2, numb3 = attributeList.index(rows[0][0]), attributeList.index(rows[1][0]), attributeList.index(rows[2][0])
		vector[2+numb1], vector[2+N+numb2], vector[2+2*N+numb3] = 1, 1, 1
	#print(vector)
	return vector 
def exponetial(theta_k, x):
	return math.exp(np.dot(theta_k, x))
def probCalc(label, labList, x, theta, z):
	rowLabIndex = labList.index(label)
	nomin = exponetial(theta[rowLabIndex], x)
	denomin = 0
	for row in theta:
		denomin += exponetial(row, x)
	return float(nomin)/float(denomin)
def Gradient(x, z, rows, attributeList, label, labList, theta, feature_flag):
	if feature_flag == 1:
		Determinter = float(rows[1] == label)
	elif feature_flag == 2:
		Determinter = float(rows[1][1] == label)
	rowLabIndex = labList.index(label)
	nomin = exponetial(theta[rowLabIndex], x)
	Prob = float(nomin)/float(z)
	result = -(Determinter-Prob)*x
	return result
# theta = theta - gradiant 	
def SGD(theta, rows, attributeList, labList, feature_flag):
	N = len(labList)
	M = len(attributeList)
	obtFunc = [ ]
	if feature_flag == 1:
		x = xVector1(rows, attributeList)
	if feature_flag == 2:
		x = xVector2(rows, attributeList)
	z = 0
	for row in theta:
		z += exponetial(row,x)
	for i in range(N):
		sgd = Gradient(x, z, rows, attributeList, labList[i], labList, theta, feature_flag)
		obtFunc.append(sgd)
	obtFunc = np.array(obtFunc)
	#print(obtFunc)
	theta -= 0.5*obtFunc
	#print(theta[0])
	return theta
def sgdLoop(theta, attribute, labList, tvsFile, feature_flag):
	time1 = time.time()
	if feature_flag == 1:
		for row in tvsFile:
			if row == [ ]:
				pass				
			else:
				theta = SGD(theta, row, attributeList, labList, feature_flag)
	elif feature_flag == 2:
		for i in range(len(tvsFile)):
			if tvsFile[i] == []:
				pass
			else:
				rows = [tvsFile[i-1], tvsFile[i], tvsFile[i+1]]
			#print(rows)
				theta = SGD(theta, rows, attributeList, labList, feature_flag)
	time2 = time.time()
	print(time1 - time2)
	return theta

#######################################
# calculate the error rate 
# calculate the most probabity and output the lab 
def evaluation(theta, x, labList):
	maxLab = [ ]
	maxProb = 0
	probValues = []
	for theta_k in theta:
		probValues.append(exponetial(theta_k, x))
	for element in probValues:
		if element > maxProb:
			maxProb = element 
			index = probValues.index(element)
			maxLab = [labList[index]]
		elif element == maxProb:
			index = probValues.index(element)
			maxLab += [labList[index]]
	return min(maxLab)

def labelList(tvsFile, theta, attributeList, labList, feature_flag):
	labels = []
	if feature_flag == 1:		
		for row in tvsFile:
			if row == [ ]:
				labels.append("\n")
			else:
				x = xVector1(row, attributeList)
				lab = evaluation(theta, x, labList)
				labels.append(lab)
	elif feature_flag == 2:
		for i in range(len(tvsFile)):
			if tvsFile[i] == []:
				labels.append("\n")
			else:
				rows = [tvsFile[i-1], tvsFile[i], tvsFile[i+1]]
				x = xVector2(rows, attributeList)
				lab = evaluation(theta, x, labList)
				labels.append(lab)
	return labels

def error(labels, tvsFile):
	totCount = 0
	errorCount = 0
	#print(len(labels), len(tvsFile))
	for i in range(len(labels)):
		if labels[i] == "\n":
			continue
		totCount +=1
		#print(labels[i], tvsFile[i][1])
		if labels[i] != tvsFile[i][1]:
			errorCount += 1
	return float(errorCount)/float(totCount)

def likelihood(theta, tvsFile, labList, attributeList, feature_flag):
	J_theta = 0
	N = 0 
	if feature_flag == 1:
		for i in range(len(tvsFile)):
			if tvsFile[i] == []:
				continue
			else:
				N += 1
				# print(tvsFile[i])
				x_i = xVector1(tvsFile[i], attributeList)
				z = 0 
				for row in theta:
					z += exponetial(row, x_i)
				for j in range(len(labList)):
					nomin = exponetial(theta[j], x_i)
					prob = float(nomin)/float(z)
					Determinter = float(tvsFile[i][1]==labList[j])
					J_theta += Determinter*math.log(prob)
	elif feature_flag == 2:
		for i in range(len(tvsFile)):
			if tvsFile[i] == []:
				continue
			else:
				N += 1
				rows = [tvsFile[i-1], tvsFile[i], tvsFile[i+1]]
				#print(rows)
			x_i = xVector2(rows, attributeList)
			z = 0
			for row in theta:
				z += exponetial(row, x_i)
			for j in range(len(labList)):
				nomin = exponetial(theta[j], x_i)
				prob = float(nomin)/float(z)
				Determinter = float(tvsFile[i][1]==labList[j])
				J_theta += Determinter*math.log(prob)
	return (-1.0/N*J_theta)

#######################################
# file output 
def labOutput(outFile, labels):
	with open(outFile, "w") as output:
		for i in range(1,len(labels)):
			if labels[i] =="\n":
				output.write("\n")
			else:
				output.write(labels[i]+"\n")
		output.close()

def Output(theta, train_tvsFile, validation_tvsFile, test_tvsFile, labList, attributeList, feature_flag, num_epoch, metrics_out):
	train_likelihood = []
	validation_likelihood = []
	for i in range(num_epoch):
		theta = sgdLoop(theta, attributeList, labList, train_tvsFile, feature_flag)
		train_like = likelihood(theta, train_tvsFile, labList, attributeList, feature_flag)
		vali_like =  likelihood(theta, validation_tvsFile, labList, attributeList, feature_flag)
		train_likelihood.append(train_like)
		validation_likelihood.append(vali_like)
	labels_train = labelList(train_tvsFile, theta, attributeList, labList, feature_flag)
	labOutput(train_out,labels_train)
	labels_test = labelList(test_tvsFile, theta, attributeList, labList, feature_flag)
	labOutput(test_out, labels_test)
	err_train = error(labels_train, train_tvsFile)
	err_test = error(labels_test, test_tvsFile)
	print(err_train, err_test)
## output metrics
	with open(metrics_out, "w") as metricsOut:
		for i in range(num_epoch):
			metricsOut.write("Epoch="+str(i+1)+" "+"likelihood(train)" + ":" + " "+ str(train_likelihood[i])+"\n")
			metricsOut.write("Epoch="+str(i+1)+" "+"likelihood(validation)" + ":" + " "+str(validation_likelihood[i])+"\n")
		metricsOut.write("Error(train):" + " " + str(err_train)+"\n")
		metricsOut.write("Error(test):" + " " + str(err_test)+"\n")
	metricsOut.close()

#######################################
if __name__ == '__main__':
   	train_input = sys.argv[1]
   	validation_input = sys.argv[2]
   	test_input = sys.argv[3]
   	train_out = sys.argv[4]
   	test_out = sys.argv[5]
   	metrics_out = sys.argv[6]
   	num_epoch = int(sys.argv[7])
   	feature_flag = int(sys.argv[8])
 # read data  	
   	train_tvsFile = readfile(train_input)
	validation_tvsFile = readfile(validation_input)
	test_tvsFile = readfile(test_input)

 # training procdure
 	attributeList, labList = makelist(train_tvsFile)
 	print(len(attributeList), len(labList))
 	theta = np.zeros((len(labList), len(attributeList)+1))
# add two features 
	if feature_flag == 2:
		theta = np.zeros((len(labList), 3*len(attributeList)+3))

		
########loop through num_epoch

	#print(error(labels_train, train_tvsFile))
	#print(error(labels_test, test_tvsFile))
	Output(theta, train_tvsFile, validation_tvsFile, test_tvsFile, labList, attributeList, feature_flag, num_epoch, metrics_out)
	







