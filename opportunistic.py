import scipy.special
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

number_of_experiments = 100
max_number_of_attacker_relays = 100
n=3200
k=3

truncate_point = 0.0009
sample_set = list(range(1,n+1))  
number_of_neighbors_2d = []            
means = []

thefile = open('opportunistic.exp.dat', 'w')
thefile2 = open('opportunistic.upper.dat', 'w')
thefile3 = open('opportunistic.lower.dat', 'w')

seed = datetime.now().microsecond
print("Seed: ", seed)
random.seed(seed)

thefile.write("%%Seed=%i\n" % (seed))
thefile2.write("%%Seed=%i\n" % (seed))
thefile3.write("%%Seed=%i\n" % (seed))

for m in range(2,max_number_of_attacker_relays+1):
	number_of_neighbors_1d = []
	for trial in range(1,number_of_experiments+1):                         
		list_of_randomly_selected_attacker_relays = sorted(random.sample(sample_set, m))
		neighbor = 0
		for i in range(0,m-2):
			number_of_hops = list_of_randomly_selected_attacker_relays[i+1] - list_of_randomly_selected_attacker_relays[i] - 1
			if number_of_hops < k:
				neighbor+=1
		number_of_hops = (list_of_randomly_selected_attacker_relays[0]+n) - (list_of_randomly_selected_attacker_relays[m-1]) - 1
		if number_of_hops < k:
				neighbor+=1
		number_of_neighbors_1d.append(0 if neighbor>0 else 1)
	number_of_neighbors_2d.append(number_of_neighbors_1d)
	mean_neighbor = sum(number_of_neighbors_1d)
	denominator = number_of_experiments
	value = np.mean(number_of_neighbors_1d)
	means.append(value)
	stdd = np.std(number_of_neighbors_1d)
	thefile.write("%i\t%f\n" % (m-1, value))
	thefile2.write("%i\t%f\n" % (m-1, value+2*stdd if value+2*stdd > truncate_point else truncate_point))
	thefile3.write("%i\t%f\n" % (m-1, value-2*stdd if value-2*stdd > truncate_point else truncate_point))
#xlabels = list(range(2,max_number_of_attacker_relays))
#plt.plot(means)
#plt.xticks(xlabels)
#plt.ylabel('Average number of less than k-hop-neighbor attacker relays (simulation)')
#plt.xlabel('Number of attacker relays, coalition (simulation)')
#plt.savefig('Average simulation np.png')
#plt.clf()
thefile.close()
thefile2.close()
thefile3.close()

#for xe, ye in zip(xlabels, number_of_neighbors_2d):
#plt.boxplot(number_of_neighbors_2d, xlabels)
#plt.xticks(xlabels)
#plt.ylabel('Number of less than k-hop-neighbor attacker relays (simulation)')
#plt.xlabel('Number of attacker relays, coalition (simulation)')
#plt.savefig('Distribution_for_100_trials.png')
#plt.clf()

#probability_formula = []
#denomenator_formula = 0.0
#numerator_formula = 0.0
#for m in range(2,max_number_of_attacker_relays):
#	numerator_formula = scipy.special.binom(n-k*m-1,m-1)
#	denomenator_formula = scipy.special.binom(n-1, m-1)
#	probability_formula.append(numerator_formula/denomenator_formula)
#plt.plot(probability_formula)
#plt.plot(means)
#plt.xticks(xlabels)
#plt.ylabel('Probability (formula)')
#plt.xlabel('Number of attacker relays, coalition (formula)')
#plt.savefig('Probability from formula.png')
#plt.clf()
