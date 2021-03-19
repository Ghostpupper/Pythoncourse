def makeclosure(par,plus):
	def power(p):
	    return p ** par + plus
	return power

fsqr = makeclosure(2,0)
fcub = makeclosure(3,1)
print(fsqr)
for i in range(5):
	print(i, fsqr(i), fcub(i))