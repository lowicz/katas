def combos(n):
	array = []
	def sub_combos(n):
		sub_array = []
		for i in range(n, 0, -1):
			if i == n:
				sub_array.append(n)
			else:
				sub_array.extend([sub_combos(x-1) for x in range (0, n)])
			#rint(sub_array)
		return sub_array
	print(sub_combos(n))
	return array.append(sub_combos(n))

print(combos(3))

# [[1], [2, [[1]]]]

#
#[[4], [1, 3], [1,1,2], [1,1,1,1] [2,2]]