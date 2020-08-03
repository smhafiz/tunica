import scipy.special

def increment(indices,m,j,k,binom):
#	print('increment method line 4: ', indices)
	indices[m-2]+=1
#	print('increment method line 6: ', indices)
	if indices[m-2] <= k:
		return indices,j,binom
	else:
		tmp = m-2
		while indices[tmp] >= k and tmp>=1:
			tmp-=1
		indices[tmp]+=1
	if m-1-j>tmp:
		j += 1
		j2 = 0
		j2+=j
		binom = scipy.special.binom(m,j2)
	for i in range(tmp+1,m-1):
		indices[i] = indices[tmp]
	print(j)
	print('increment method line 22: ', indices)
	return indices,j,binom

n=3200
k=3
m=10

indices,binom,j = increment([0 for i in range(m-1)],m,1,k,0)
total = 0
print('main line 31: ', indices)
while indices[0]<=k:
	total += scipy.special.binom(n-k*m+i-j-1,m-j-1)#*binom
	indices,binom,j = increment(indices,m,j,k,binom)
total /= scipy.special.binom(n-1,m-1)
print(total)
