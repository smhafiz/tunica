import scipy.special
import matplotlib.pyplot as plt

n=3200
k=3
max_number_of_attacker_relays = 100

def incr(indices,ell,oldbinom):
	indices[0] += 1
	if indices[0] <= k:
		return indices,sum(indices),ell,oldbinom
	else:
		i = next(i for i,v in enumerate(indices) if v < k)
		indices[i] += 1
		indices[0:i] = [indices[i]] * i
		return indices,sum(indices),i if i>ell else ell,scipy.special.binom(m,i) if i>ell else oldbinom

def findCoverage(n,k,m):
	partialsum=0
	indices,weight,ell,binomial = incr([0 for i in range(m)], 1, scipy.special.binom(m,1))
	while indices[m-1] == 0:
		#print(indices)
		partialsum += scipy.special.binom(n-k*m+weight-ell-1,m-ell-1)*binomial*weight
		indices,weight,ell,binomial = incr(indices,ell,binomial)

	return (partialsum/scipy.special.binom(n-1,m-1))

results_2d = []
for m in range(2,max_number_of_attacker_relays):
	results_2d.append(findCoverage(n,k,m))
#print(results_2d)
xlabels = list(range(2,max_number_of_attacker_relays))
plt.plot(results_2d)
plt.xticks(xlabels)
plt.ylabel('Expected coverage')
plt.xlabel('Number of attacker relays, coalition')
plt.savefig('Distribution.png')
plt.clf()
