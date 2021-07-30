from hungarian_algorithm import algorithm as hun_alg
from scipy.optimize import linear_sum_assignment
import numpy as np
import random, string, copy


# H_ = [   [9,2,3,3,8,10,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[8,1,1,2,2,4,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[9,5,5,3,8,10,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[6,1,8,2,4,3,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[9,2,5,8,8,10,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,7,3,3,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20],
# 		[4,1,8,3,7,8,2,3,6,3,4,5,6,2,3,12,3,2,3,20]

# ]
# H_ = [   [9,2,3,],
# 		[8,1,1],
# 		[4,1,8],
# 		[4,1,8]

# # ]
# H_ = np.array(H_)


# row_ind, col_ind = linear_sum_assignment(H_)

# print(H_, H_[row_ind, col_ind].sum())
# row_ind = np.array(row_ind).tolist()
# col_ind = np.array(col_ind).tolist()
# print(row_ind, col_ind)
# # print(len(row_ind), len(col_ind))
# reslt = []
# H_ = np.array(H_).tolist()
# # print(H_)

		

# for i in range(len(row_ind)):
# 	reslt.append(H_[row_ind[i]][col_ind[i]])
# 	# print(reslt[-1])

# print(sum(reslt))
rs = ['A', 'B', 'C']
ppl = [1, 2, 3, 4, 5, 6, 7]

def virtual_weights(A, B, age=None):
    # consider age, distance A, B
    return random.randrange(1, 10)

# H = [[None for j in range(len(rs))] for i in range(len(ppl))]
# for p in range(len(ppl)):
# 	for r in range(len(rs)):
# 		H[p][r] = virtual_weights(p+1, r+1)#rs[r], ppl[p])
# print(H)



def solve(res_stf, a_ppl):
	r_len = 3
	a_len = 7
	H = [[15, 1, 35], [15, 1, 85], [15, 1, 15], [15, 1, 75], [15, 1, 105], [9, 1, 25], [15, 1, 8]]
	H_ = np.array(H)
	reslt = {}
	reslt_rescue = {}
	while len(reslt) < max(r_len, a_len):
		row_ind, col_ind = linear_sum_assignment(H_)
		
		H_ = np.array(H_).tolist()
		# print(H_)
		row_ind = np.array(row_ind).tolist()
		col_ind = np.array(col_ind).tolist()

		for i in range(len(row_ind)):
			if ppl[row_ind[i]] not in reslt:
				reslt[ppl[row_ind[i]]] = [rs[col_ind[i]], H_[row_ind[i]][col_ind[i]]]
				if rs[col_ind[i]] in reslt_rescue:
					reslt_rescue[rs[col_ind[i]]] += 1
				else:
					reslt_rescue[rs[col_ind[i]]] = 1
			H_[row_ind[i]][col_ind[i]] = 99
	for each in reslt:
		print(each, reslt[each])
	for each in reslt_rescue:
		print(each, reslt_rescue[each])
ppl_new = [1,2,3,4,56]
ppl_new.reverse()
print(ppl_new)