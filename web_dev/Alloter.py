from hungarian_algorithm import algorithm as hun_alg
import random, string, copy

res_stf = ['A', 'B', 'C']
ppl = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22]


# ppl = [1]

def virtual_weights(A, B, age=None):
    # consider age, distance A, B
    return random.randrange(1, 10)

def create_minMap(target, rs, real_count=0):
    tmp = {}
    n = len(rs)
    # real value calculation
    for i in range(real_count):
        if type(target) == int:
            tmp[rs[i]] = virtual_weights(rs[i], target)
        else:
            tmp[rs[i]] = random.randrange(950, 1000)
    # infinity for dummies
    for i in range(real_count, n):
        tmp[rs[i]] = random.randrange(950, 1000)
    return copy.deepcopy(tmp)


def virtual_name():
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=7))
    return res

def create_map_assist(r, s):
    real_count = len(r)
    extras = len(r) - len(s)

    for i in range(extras):
        s.append(virtual_name())
    H = {}
    # create a graph
    for s_ in s:
        H[s_] = create_minMap(s_, r, real_count=real_count)

    return copy.deepcopy(H)


def create_map(rstaff, surv):
    # precaution to prevent the manipulation of argument array+
    r = copy.deepcopy(rstaff)
    s = copy.deepcopy(surv)

    # make sure people are more than rescue staff
    if len(r) > len(s):
        print("Oh! Rescue people is more than people, Verify the rsults once and delete create_Map 3rd line")
        return create_map_assist(r, s)
    # Add Dummies and keep count
    real_count = len(r)
    extras = len(s) - len(r)
    for i in range(extras):
        r.append(virtual_name())

    H = {}
    # create a graph
    for s_ in s:
        H[s_] = create_minMap(s_, r, real_count=real_count)

    # print(r)
    # for i in range(len(H)):
    #     print(i + 1, H[i + 1])
    return copy.deepcopy(H)


def solve(R_s, A_p):
	print("Solving...")
	R_staff = copy.deepcopy(R_s)
	A_ppl = copy.deepcopy(A_p)
	results = {}
	# print('R_staff:', R_staff, 'PPL:', A_ppl)
	while (len(A_ppl) != 0):
		# print('Next round->')
		G = create_map(R_staff, A_ppl)
		# print(R_staff, A_ppl)
		x = hun_alg.find_matching(G, matching_type='min', return_type='list')
		for each in x:
			if each[-1] < 950:
				# print(each[0])
				if each[0][1] in results:
					results[each[0][1]].append(each[0][0])
				else:
					results[each[0][1]] = [each[0][0]]
			    # if each[0][1] in R_staff:
			    # 	R_staff.remove(each[0][1])
				if each[0][0] in A_ppl:
					A_ppl.remove(each[0][0])
	print("After Allotment", R_staff, A_ppl)
	return results


print(res_stf, ppl)
G = create_map(res_stf, ppl)
# for each in G:
#     print(each,G[each])
# x = hun_alg.find_matching(G, matching_type='min', return_type='list')
# print('completed')
# for each in x:
#     if each[-1] < 950:
#         print(each[0])
        # if each[0][1] in res_stf:
        #     res_stf.remove(each[0][1])
        # if each[0][0] in ppl:
        #     ppl.remove(each[0][0])
while True:
    try:
        answer = solve(res_stf, ppl)
        break
    except:
        continue

print(answer)