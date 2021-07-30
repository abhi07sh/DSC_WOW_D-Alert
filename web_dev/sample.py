import pyrebase, folium
import random
# from flaskblog.active_users import User as user_x
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



# returns all pairs of locs[ppl to rstaff]
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

# create a new base camp

# name = "Nandi petrol"
# loc_base = [76.6326642036438, 12.315621979013098]
# supplies  = "Food packets, Water Bottles, First aid kits"


# archer = {"Name": name, "Location": "lat/lng: ("+str(loc_base[1])+","+str(loc_base[0])+")", "Supplies": supplies, 'Base_id' : 'X'}
# db1.child("Base_camps").push(archer)


# db1.child('Base_camps').child('-MVkNr4lsICQbjIec6X_').update({'Supplies' : supplies})

# x = db1.child('Rescue_staff').get()
# ids = x.val().keys()


# # item = db1.child('Rescue_staff').child('-MWG2b3ClkAJyB1xYZC-').get().val()
# x = db1.child('Rescue_staff').get()
# item = x.val().get('-MWG2b3ClkAJyB1xYZC-')
# print(item)
# lat_lng_2 = item['Location'].split()[1]\
#     .strip('(').strip(')').split(',')

# lat_lng_2 = list(map(float, lat_lng_2)) 

# print(lat_lng_2)

# db1.child('Rescue_staff').child("-MWG2axw0WlorOyHgilR").update({"contact": 8073211825})

# Complete User details
# # db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"isRescued": False})   #set isrescued false by id
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"rescued_By": ""})
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"user_id": 9})
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"Age": 20})




# age = "self"
# tmp = [ 'moo','foo_2', 'moo_2','last_try']
# db1.child('Base_camps').child("").update({"isRescued": False})
# print("sample.py executing")
# for id in ids:
#     rsppl_data = db1.child('Rescue_staff').child(id).child('willRescue').get().val()
#     if rsppl_data is None:
#         op = tmp
#     else:
#         op = rsppl_data + tmp   
#     op = list(set(op))
#     db1.child('Rescue_staff').child(id).update({"willRescue": op})

#     print(rsppl_data)




    # keys = rsppl_data.val().keys()
    # for each in keys:
    #     print(rsppl_data[each])
    # db1.child('flask_app').child(id).update({"rescued_By": age})

    # print(x.val().get(id)['Name'], x.val().get(id)['willRescue'])

# archer = {"Name": "Tony Stark", "Location": "lat/lng: (12.331587,76.6139528)", "rescue_id":'1'}
# db1.child("Rescue_staff").push(archer)
# archer = {"Name": "Peter Parker", "Location": "lat/lng: (12.321784,76.6129504)", "rescue_id":'1'}
# db1.child("Rescue_staff").push(archer)
# archer = {"Name": "Peter Parker", "Location": "lat/lng: (12.711787,76.1129524)"}
# db1.child("Rescue_staff").push(archer)
# archer = {"Name": "Peter Parker", "Location": "lat/lng: (12.711787,76.1129524)"}
# db1.child("Rescue_staff").push(archer)

# # db1.commit()


# ---------------------------------------------------------------------------------
# token = None
# map_key = None
# users = []
# i = 0
# if token==None or token == 'S':
#     x = db1.child("flask_app").get()
#     ids = x.val().keys()


#     for prime_key in ids:
#         raw = x.val().get(prime_key)
#         designation = 'S'
#         lat_lng = raw['Location'].split()[1] \
#             .strip('(').strip(')').split(',')
#         lat_lng = list(map(float, lat_lng))
#         # print(lat_lng)
#         name = raw['Name']
#         user = user_x(prime_key, i, name, designation, lat_lng)
#         # print(user.prime_key, user.id_x, user.designation, user.loc_data)
#         users.append(user)
#         i += 1
# if token==None or token == 'R':
#     # update as rescue staff
#     x = db1.child("Rescue_staff").get()
#     ids = x.val().keys()


#     for prime_key in ids:
#         raw = x.val().get(prime_key)
#         designation = 'R'
#         lat_lng = raw['Location'].split()[1] \
#             .strip('(').strip(')').split(',')
#         lat_lng = list(map(float, lat_lng))
#         # print(lat_lng)
#         name = raw['Name']
#         user = user_x(prime_key, i, name, designation, lat_lng)
#         # print(user.prime_key, user.id_x, user.designation, user.loc_data)
#         users.append(user)
#         i += 1

# if token==None or token == 'B':
#     # update as basecamp
#     x = db1.child("Base_camps").get()
#     ids = x.val().keys()


#     for prime_key in ids:
#         raw = x.val().get(prime_key)
#         designation = 'B'
#         lat_lng = raw['Location'].split()[1] \
#             .strip('(').strip(')').split(',')
#         lat_lng = list(map(float, lat_lng))
#         # print(lat_lng)
#         name = raw['Name']
#         user = user_x(prime_key, i, name, designation, lat_lng)
#         # print(user.prime_key, user.id_x, user.designation, user.loc_data)
#         users.append(user)
#         i += 1
# for user in users:
#     print(user.designation, user.name)
# # tile = folium.Icon(color='green')

# map_x = folium.Map(
#     width=1000,height=650,
#     location=users[-1].loc_data,
#     tiles="Stamen Terrain",
#     zoom_start=13.5
# )
# for user in users:
#     # tr = ''
#     # tip = [each.name for each in user.neighbours

#     if (map_key == None or map_key == "R") and user.designation == 'R':
#         tip = str(user.name)
#         icon = folium.Icon(color='blue')
#         print("blue")
#     elif (map_key == None or map_key == "S") and user.designation == 'S':
#         tip = str(user.name)
#         icon = folium.Icon(color='red')
#         print("red")
#     # elif (map_key == None or map_key == "B") and user.designation == 'B':
#     #     tip = 'Base Camp'
#     #     icon = folium.Icon(color='green')
#     #     print("green")
#     folium.Marker(
#         location=user.loc_data,
#         popup="<b>" + str(user.name) + "</b>",
#         tooltip=tip,
#         icon=icon
#     ).add_to(map_x)
# map_x.save("sample.html")
# folium.TileLayer('Stamen Terrain').add_to(map_x)
# folium.TileLayer('Stamen Toner').add_to(map_x)
# folium.TileLayer('Stamen Water Color').add_to(map_x)
# folium.TileLayer('cartodbpositron').add_to(map_x)
# folium.TileLayer('cartodbdark_matter').add_to(map_x)
# folium.LayerControl().add_to(map_x)
# map_x = add_markers(users, map_x, token)

cords = [[76.61779403686523, 12.34587110791957], [76.64011001586914, 12.30226765006948],
 [76.61727905273438, 12.319206777401684], [76.6157341003418, 12.29555878278311],
  [76.65573120117188, 12.276102099723333], [76.61762237548828, 12.263521582276313],
 [76.6622543334961, 12.316858844809435], [76.66980743408203, 12.261844134568571],
  [76.69538497924805, 12.281469604268654], [76.65058135986328, 12.29069474693012],
   [76.68474197387694, 12.292539736638817], [76.69795989990234, 12.314343179433545],
   [76.68886184692383, 12.328598297611613], [76.68113708496092, 12.298242350248833],
  [76.67203903198242, 12.342181865458057], [76.64989471435545, 12.317697394575683],
   [76.63959503173828, 12.342852640681242], [76.6189956665039, 12.32239322373886],
    [76.66997909545898, 12.32323175581517],  [76.63564682006836, 12.26201187981968],
   [76.62174224853516, 12.280127738392657], [76.61779403686523, 12.34587110791957]]

cords = random.sample(cords, 12)
print(len(cords))
name = "rescue_"
isRescued = False

rescued_By = ""
rescue_id = 4
contact = 9876543210

# color = "#"+''.join([random.choice('0123456789ABCD') for j in range(6)])
# print(color)




for location in cords:
    n_name = name + str(rescue_id)
    age = random.randrange(8, 70)
    archer = {"Name": n_name,
     "Location":"lat/lng: ("+str(location[1])+","+str(location[0])+")",
     "rescue_id":rescue_id,
     "contact": contact,
     "willRescue" : [0]}
    rescue_id += 1
    db1.child("Rescue_staff").push(archer)
    print("pushed")






# Complete User details
# # db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"isRescued": False})   #set isrescued false by id
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"rescued_By": ""})
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"user_id": 9})
# db1.child('flask_app').child("-MW_gp6Z30-t1ZXyTv3k").update({"Age": 20})