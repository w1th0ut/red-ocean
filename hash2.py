import sha3
import itertools

exploit = '64723e4e97cadec37d38779993e427ee7b491121f53fe634271741aadf4d0c50'

start = 5
end = 5

chrs = 'abcdefghijklmnopqrstuvwxyz'
chrs_up = chrs.upper()
chrs_specials = "!_#$*&*. "
chrs_numerics = '1234567890'
chrs = ''.join([chrs, chrs_up])
chrs = ''.join([chrs, chrs_specials])
chrs = ''.join([chrs, chrs_numerics])

for i in range(start, end+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		data = sha3.keccak_256()
		data.update(temp)
		key = data.hexdigest()
		#print temp
		#print key
		if key == exploit:
			print ("Key Found: ")
			print temp
			break
