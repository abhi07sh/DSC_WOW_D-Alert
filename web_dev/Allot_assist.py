from scipy.optimize import linear_sum_assignment
import numpy as np
import random, string, copy
from collections import OrderedDict


def virtual_weights(A, B, age=None):
    # consider age, distance A, B
    return random.randrange(1, 10)




def create_map(rs, ppl):
    # precaution to prevent the manipulation of argument array+
    # rs = copy.deepcopy(rstaff)
    # ppl = copy.deepcopy(surv)
	H = [[None for j in range(len(rs))] for i in range(len(ppl))]
	for p in range(len(ppl)):
		for r in range(len(rs)):
			H[p][r] = dist_calcy(rs[r], ppl[p])
		print(H[p])

	return H

def solve(R_s, A_p):
	r_len = len(R_s)
	a_len = len(A_p)
	print("Solving...")
	rs = copy.deepcopy(R_s)
	ppl = copy.deepcopy(A_p)
	H = create_map(rs, ppl)
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
	# print(sorted(reslt.items(), key= lambda x:x[0]))
	reslt = OrderedDict(sorted(reslt.items()))
	for each in reslt:
		print(each, reslt[each])
	for each in OrderedDict(sorted(reslt_rescue.items())):
		print(each, reslt_rescue[each])

	return reslt



res_stf = ['A', 'B', 'C']
ppl = [1, 2, 3, 4,5,6,7,8,9]
answer = solve(res_stf, ppl)
# print(answer)