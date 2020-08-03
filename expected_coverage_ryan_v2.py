import scipy.special
import math
import matplotlib.pyplot as plt

n=3200
k=3
max_number_of_attacker_relays = 101

def multinomial(indices):
	multinom = math.factorial(m)
	for i in range(k+1):
		multinom /= math.factorial(indices.count(i))
	return multinom

def incr(indices,ell):
	indices[0] += 1
	if indices[0] <= k:
		return indices,sum(indices),ell if ell>0 else 1,multinomial(indices)
	else:
		i = next(i for i,v in enumerate(indices) if v < k)
		indices[i] += 1
		indices[0:i] = [indices[i]] * i
		return indices,sum(indices),i+1 if i>=ell else ell,multinomial(indices)

def findCoverage(n,k,m):
	partialsum=0
	indices,weight,ell,multinom = incr([0 for i in range(m)],1)
	while indices[m-1] == 0:
		partialsum += scipy.special.binom(n-k*m+weight-ell-1,m-ell-1)*multinom*weight
		indices,weight,ell,multinom = incr(indices,ell)

	return (partialsum/scipy.special.binom(n-1,m-1))

thefile = open('Data_Values_Formula.txt', 'w')
results_2d = []
for m in range(2,max_number_of_attacker_relays):
	tmpp = findCoverage(n,k,m)
	results_2d.append(tmpp)
	thefile.write("%f\n" % tmpp)
thefile.close()
#print(results_2d)
xlabels = list(range(2,max_number_of_attacker_relays))
plt.plot(results_2d)
plt.xticks(xlabels)
plt.ylabel('Expected coverage')
plt.xlabel('Number of attacker relays, coalition')
plt.savefig('Distribution_v2.png')
plt.clf()
