import pyrebase
from math import radians, cos, sin, asin, sqrt
from scipy.optimize import linear_sum_assignment
import numpy as np
import random, string, copy
from collections import OrderedDict

firebaseConfig = {
    'apiKey': "AIzaSyDSmHLO48eQvr8i6f-e9Bj0dmGlqlWkLxw",
    'authDomain': "disastermangement-1de94.firebaseapp.com",
    'databaseURL': "https://disastermangement-1de94-default-rtdb.firebaseio.com",
    'projectId': "disastermangement-1de94",
    'storageBucket': "disastermangement-1de94.appspot.com",
    'messagingSenderId': "366752650310",
    'appId': "1:366752650310:web:ab01a77a8f22827320e647",
    'measurementId': "G-Q47TZ3RH7Y"
}
firebase = pyrebase.initialize_app(config=firebaseConfig)
db1 = firebase.database()

# Check Internet Connection
import socket

REMOTE_SERVER = "one.one.one.one"


def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


if not is_connected(REMOTE_SERVER):
    print("No Internet Connection")
    # exit()


class FB_User:
    def __init__(self, id, index, designation, loc_data, name, isDone=False, age=0, supplies="Nothing", contact=0, rescue_strength=0):
        self.prime_key = id
        self.id_x = index
        self.age = age
        self.name = name
        self.isDone = isDone
        self.contact = contact
        self.designation = designation
        self.loc_data = loc_data
        self.rescue_strength = rescue_strength
        self.supplies = supplies
        self.neighbours = []

    def __repr__(self):
        return f"{self.name}"
        return f"{self.prime_key}, {self.name}, {self.designation}, {self.loc_data}"


def get_ppl():
    x = db1.child('flask_app').get()
    ids = x.val().keys()
    ppl_list = []

    for prime_key in ids:
        raw = x.val().get(prime_key)

        isRescued = raw['isRescued']
        # print(raw['Name'], isRescued)
        if isRescued == "false":
            continue
        designation = 's'
        lat_lng = raw['Location'].split()[1] \
            .strip('(').strip(')').split(',')
        lat_lng = list(map(float, lat_lng))
        # print(lat_lng)
        name = raw['Name']
        user_id = raw['user_id']
        user = FB_User(prime_key, user_id, designation, lat_lng, name)
        # print(user.prime_key, user.name, user.loc_data, isRescued)
        ppl_list.append(user)

    # print(ppl_list)
    return ppl_list


def get_rstaff():
    x = db1.child('Rescue_staff').get()
    ids = x.val().keys()
    ppl_list = []
    i = 0

    for prime_key in ids:
        raw = x.val().get(prime_key)
        designation = 'r'
        lat_lng = raw['Location'].split()[1] \
            .strip('(').strip(')').split(',')
        lat_lng = list(map(float, lat_lng))
        # print(lat_lng)
        name = raw['Name']
        rs_id = raw['rescue_id']
        user = FB_User(prime_key, rs_id, designation, lat_lng, name)
        # print(user.prime_key, user.name, user.loc_data, isRescued)
        ppl_list.append(user)

    return ppl_list

# returns all pairs of locs[rstaff to ppl]
def get_allCalls_by_rstaff():
    x = db1.child('Rescue_staff').get()
    ids = x.val().keys()
    call_list = []
    # print("keys :", ids)

    for prime_key in ids:
        raw = x.val().get(prime_key)
        # print(raw)
        lat_lng = raw['Location'].split()[1] \
            .strip('(').strip(')').split(',')
        lat_lng = list(map(float, lat_lng))
        # print(lat_lng)

        to_rescued = raw['willRescue']

        # print(to_rescued)
        sub_keys = []
        for each in to_rescued:
            px = db1.child('flask_app').get()
            raw_2 = px.val().get(each)
            # print('raw_2', raw_2)
            if raw_2 is None:
                continue
            lat_lng_2 = raw_2['Location'].split()[1] \
            .strip('(').strip(')').split(',')
            lat_lng_2 = list(map(float, lat_lng_2))
            sub_keys.append(lat_lng_2)
            # print(lat_lng_2)
        if len(sub_keys) > 0:
            call_list.append([lat_lng, sub_keys])
        # isRescued = raw['isRescued']
        # if isRescued:
        #     continue

        # hero = raw['rescued_By']
        # rx = db1.child('Rescue_staff').get()
        # item = rx.val().get(hero)
        # lat_lng_2 = item['Location'].split()[1] \
        #     .strip('(').strip(')').split(',')

        # lat_lng_2 = list(map(float, lat_lng_2))
        # # print(user.prime_key, user.name, user.loc_data, isRescued)
        # call_list.append([lat_lng, lat_lng_2])

    # print(len(call_list))

    return call_list


# returns all pairs of locs[ppl to rstaff]
def get_allCalls():
    x = db1.child('flask_app').get()
    ids = x.val().keys()
    call_list = []
    # print("keys :", ids)

    for prime_key in ids:
        raw = x.val().get(prime_key)
        # print(raw)
        isRescued = raw['isRescued']
        if isRescued:
            continue
        lat_lng = raw['Location'].split()[1] \
            .strip('(').strip(')').split(',')
        lat_lng = list(map(float, lat_lng))
        # print(lat_lng)
        hero = raw['rescued_By']
        rx = db1.child('Rescue_staff').get()
        item = rx.val().get(hero)
        lat_lng_2 = item['Location'].split()[1] \
            .strip('(').strip(')').split(',')

        lat_lng_2 = list(map(float, lat_lng_2))
        # print(user.prime_key, user.name, user.loc_data, isRescued)
        call_list.append([lat_lng, lat_lng_2])

    # print(call_list)

    return call_list


def dist_calcy(person1, person2):
    lat1, long1 = person1.loc_data
    lat2, long2 = person2.loc_data
    # The math module contains a function named
    # radians which converts from degrees to radians.
    long1 = radians(long1)
    long2 = radians(long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return int(c * r)


def create_map(rs, ppl):
    # precaution to prevent the manipulation of argument array+
    # rs = copy.deepcopy(rstaff)
    # ppl = copy.deepcopy(surv)
    H = [[None for j in range(len(rs))] for i in range(len(ppl))]
    for p in range(len(ppl)):
        for r in range(len(rs)):
            H[p][r] = dist_calcy(rs[r], ppl[p])
        # print(H[p])

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
    reslt_new = {}
    reslt_rescue = {}
    while len(reslt) < max(r_len, a_len):
        row_ind, col_ind = linear_sum_assignment(H_)

        H_ = np.array(H_).tolist()
        # print("Matrix :")
        # for each in H_:
        #     print(each)
        # print(H_)
        row_ind = np.array(row_ind).tolist()
        col_ind = np.array(col_ind).tolist()

        for i in range(len(row_ind)):
            # print("Options :", ppl[row_ind[i]], rs[col_ind[i]])
            if ppl[row_ind[i]] not in reslt:
                reslt[ppl[row_ind[i]]] = [rs[col_ind[i]], H_[row_ind[i]][col_ind[i]]]
                reslt_new[ppl[row_ind[i]].prime_key] = rs[col_ind[i]].prime_key
                # print("paired", ppl[row_ind[i]], reslt[ppl[row_ind[i]]])
                if rs[col_ind[i]] in reslt_rescue:
                    reslt_rescue[rs[col_ind[i]]].append(ppl[row_ind[i]].prime_key)
                else:
                    reslt_rescue[rs[col_ind[i]]] = [ppl[row_ind[i]].prime_key]
            H_[row_ind[i]] = [99 for _ in range(len(col_ind))]
    # print(sorted(reslt.items(), key= lambda x:x[0]))
    # reslt = OrderedDict(sorted(reslt.items()))
    # for each in reslt:
    #     print(each, reslt[each])
    # for each in OrderedDict(sorted(reslt_rescue.items())):
    # 	print(each, reslt_rescue[each])

    # Can return reslt, reslt_new, reslt_rescue
    # reslt -> result, type-dict, key=person(ppl), value=list[rescue_person, weight]
    # reslt_new -> result, type-dict, key=person(ppl), value=rescue_person
    #
    return reslt_new, reslt_rescue
    return reslt

# pplx = get_ppl()
# print(pplx)

# rstaffx = get_rstaff()
# print(rstaffx)
# print(solve(rstaffx, pplx))
