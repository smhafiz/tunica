import scipy.special
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

truncate_point = 0.115000
number_of_experiments = 100
max_number_of_attacker_relays = 100
n=3200
k=3

sample_set = list(range(1,n+1))   
number_of_common_partitions_2d = []            
means = []

thefile = open('coverage.exp.dat', 'w')
thefile2 = open('coverage.upper.dat', 'w')
thefile3 = open('coverage.lower.dat', 'w')

seed = datetime.now().microsecond
print("Seed: ", seed)
random.seed(seed)

thefile.write("%%Seed=%i\n" % (seed))
thefile2.write("%%Seed=%i\n" % (seed))
thefile3.write("%%Seed=%i\n" % (seed))

for m in range(2,max_number_of_attacker_relays+1):
	#sum_of_number_of_common_partitions = 0.0
	number_of_common_partitions_1d = []
	for trial in range(1,number_of_experiments+1):                         
		list_of_randomly_selected_attacker_relays = sorted(random.sample(sample_set, m))
		common_partitions = 0
		for i in range(0,m-2):
			number_of_hops = list_of_randomly_selected_attacker_relays[i+1] - list_of_randomly_selected_attacker_relays[i] - 1
			if number_of_hops < k:
				common_partitions+= (k - number_of_hops)
		number_of_hops = (list_of_randomly_selected_attacker_relays[0]+n) - (list_of_randomly_selected_attacker_relays[m-1]) - 1
		if number_of_hops < k:
				common_partitions+= (k - number_of_hops)
		number_of_common_partitions_1d.append(common_partitions)
		#sum_of_number_of_common_partitions+=common_partitions
	number_of_common_partitions_2d.append(number_of_common_partitions_1d)
	#mean_common_partitions = sum_of_number_of_common_partitions/number_of_experiments
	#denominator = 1#scipy.special.binom(n-1, m-1)
	meann = np.mean(number_of_common_partitions_1d)
	means.append(meann)
	stdd = np.std(number_of_common_partitions_1d)
	thefile.write("%i\t%f\n" % (m-1, meann))
	thefile2.write("%i\t%f\n" % (m-1, meann+2*stdd if meann+2*stdd > truncate_point else truncate_point))
	thefile3.write("%i\t%f\n" % (m-1, meann-2*stdd if meann-2*stdd > truncate_point else truncate_point))
thefile.close()
thefile2.close()
thefile3.close()
#xlabels = list(range(2,max_number_of_attacker_relays))
#plt.plot(means)
#plt.xticks(xlabels)
#plt.ylabel('Average number of common partitions in attacker relays (simulation)')
#plt.xlabel('Number of attacker relays, coalition (simulation)')
#plt.savefig('Expected Coverage Average simulation.png')
#plt.clf()




#for xe, ye in zip(xlabels, number_of_common_partitions_2d):
#plt.boxplot(number_of_common_partitions_2d, xlabels)
#plt.xticks(xlabels)
#plt.ylabel('Number of common partitions in attacker relays (simulation)')
#plt.xlabel('Number of attacker relays, coalition (simulation)')
#plt.savefig('Expected Coverage Distribution_for_100_trials.png')
#plt.clf()

#probability_formula = []
#denomenator_formula = 0.0
#numerator_formula = 0.0
#for m in range(2,max_number_of_attacker_relays):
#	numerator_formula = scipy.special.binom(n-k*m-1,m-1)
#	denomenator_formula = scipy.special.binom(n-1, m-1)
#	probability_formula.append(1-numerator_formula/denomenator_formula)
#plt.plot(probability_formula)
#plt.xticks(xlabels)
#plt.ylabel('Probability (formula)')
#plt.xlabel('Number of attacker relays, coalition (formula)')
#plt.savefig('Probability from formula.png')
#plt.clf()
