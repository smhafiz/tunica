import scipy.special



def sumOfPairs(numOfSums, i, sumOfIndexes,sumOfTerms):
	global k
	if numOfSums > 1:
		#subtractTerm +=1

		for x in range(i,k):
			print(str(numOfSums)+", "+str(x))
		sumOfPairs(numOfSums-1, x, sumOfIndexes, sumOfTerms)
	else:
		print("In base")
		#return 100
		#remaining_nodes = n-k*m+sumOfIndexes-(subtractTerm+1)
		#numerator = scipy.special.binom(remaining_nodes, m - remaining_nodes)
		#denominator = scipy.special.binom(n-1, m - 1)

k=4
print(sumOfPairs(5,1,0,0))



