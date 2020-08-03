import scipy.special
import random
import numpy as np
import matplotlib.pyplot as plt

number_of_experiments = 100
max_number_of_attacker_relays = 101
n=3200
k=3

sample_set = list(range(1,n))   
number_of_neighbors_2d = []            
means = []
for m in range(2,max_number_of_attacker_relays):
	number_of_neighbors_1d = []
	for trial in range(1,number_of_experiments):                         
		list_of_randomly_selected_attacker_relays = sorted(random.sample(sample_set, m))
		neighbor = 0
		for i in range(0,m-2):
			number_of_hops = list_of_randomly_selected_attacker_relays[i+1] - list_of_randomly_selected_attacker_relays[i] - 1
			if number_of_hops < k:
				neighbor+=1
		number_of_hops = (list_of_randomly_selected_attacker_relays[0]+n) - (list_of_randomly_selected_attacker_relays[m-1]) - 1
		if number_of_hops < k:
				neighbor+=1
		number_of_neighbors_1d.append(neighbor)
	number_of_neighbors_2d.append(number_of_neighbors_1d)
	mean_neighbor = np.mean(number_of_neighbors_1d)
	denominator = 1#scipy.special.binom(n-1, m-1)
	means.append(mean_neighbor/denominator)
xlabels = list(range(2,max_number_of_attacker_relays))
plt.plot(means)
plt.xticks(xlabels)
plt.ylabel('Average number of less than k-hop-neighbor attacker relays (simulation)')
plt.xlabel('Number of attacker relays, coalition (simulation)')
plt.savefig('Average simulation np.png')
plt.clf()


#for xe, ye in zip(xlabels, number_of_neighbors_2d):
plt.boxplot(number_of_neighbors_2d, xlabels)
plt.xticks(xlabels)
plt.ylabel('Number of less than k-hop-neighbor attacker relays (simulation)')
plt.xlabel('Number of attacker relays, coalition (simulation)')
plt.savefig('Distribution_for_100_trials.png')
plt.clf()

probability_formula = []
denomenator_formula = 0.0
numerator_formula = 0.0
for m in range(2,max_number_of_attacker_relays):
	numerator_formula = scipy.special.binom(n-k*m-1,m-1)
	denomenator_formula = scipy.special.binom(n-1, m-1)
	probability_formula.append(1-numerator_formula/denomenator_formula)
plt.plot(probability_formula)
plt.xticks(xlabels)
plt.ylabel('Probability (formula)')
plt.xlabel('Number of attacker relays, coalition (formula)')
plt.savefig('Probability from formula.png')
plt.clf()
