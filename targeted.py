import scipy.special
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def find_tag(value,limit):
	result = value
	if value < 1 :
		result = limit + value
	elif value > limit:
		result = value - limit
	return result

truncate_point = 0.0009
number_of_experiments = 100
max_number_of_attacker_relays = 1000
n=3200
k=3
r=2

thefile = open('targeted.exp.dat', 'w')
thefile2 = open('targeted.upper.dat', 'w')
thefile3 = open('targeted.lower.dat', 'w')

sample_set = list(range(1,n+1))

seed = datetime.now().microsecond
print("Seed: ", seed)
random.seed(seed)

thefile.write("%%Seed=%i\n" % (seed))
thefile2.write("%%Seed=%i\n" % (seed))
thefile3.write("%%Seed=%i\n" % (seed))

for m in range(2,max_number_of_attacker_relays+1+10,10):
	total_fall_in = []
	for trial in range(1,number_of_experiments+1):
		fall_in = 0
		attacker_relays = sorted(random.sample(sample_set, m))
		replica_set_relays=[]
		for rr in range(1,r+1):
			replica_value = random.choice(sample_set)
			replica_set_relays.append(replica_value)
			for d in range(0,k):
				try: 
					sample_set.remove(find_tag(replica_value+d,n))
				except:
					pass
			for d in range(1,k):
				try: 
					sample_set.remove(find_tag(replica_value-d,n))
				except:
					pass
		sample_set = list(range(1,n+1))   		
		replica_set_relays=sorted(replica_set_relays)
		for b in replica_set_relays:
			for a in range(0,len(attacker_relays)):
				if attacker_relays[a] >= b and attacker_relays[a] < b+k:
					for c in range(a+1,len(attacker_relays)):
						if attacker_relays[c] >= b and attacker_relays[c] < b+k:
							fall_in = 1
		total_fall_in.append(fall_in)
	mean = np.mean(total_fall_in)
	stdd = np.std(total_fall_in)
	thefile.write("%i\t%f\n" % (m-1, mean))
	thefile2.write("%i\t%f\n" % (m-1, mean+2*stdd if mean+2*stdd > truncate_point else truncate_point))
	thefile3.write("%i\t%f\n" % (m-1, mean-2*stdd if mean-2*stdd > truncate_point else truncate_point))
thefile.close()
thefile2.close()
thefile3.close()

#summation = 0.0
#for e in range(0,r+1):
#	summation+=scipy.special.binom(n-r*k,m-e)*scipy.special.binom(r,i)*scipy.special.binom(k,1)
#xlabels = list(range(2,max_number_of_attacker_relays))
#plt.plot(all_fall_ins)
#plt.xticks(xlabels)
#plt.ylabel('Replica set')
#plt.xlabel('Number of attacker relays, coalition (simulation)')
#plt.savefig('targeted_attack_simulation.png')
#plt.clf()
