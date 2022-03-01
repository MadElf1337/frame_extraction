import json
import pprint

file = open("yt_walk.json", 'r')

data = json.load(file)


# pprint.pprint(data)

# key1 = "age"
# key2 = "gender"
temp = []

k = [{}]
xd=[]
for frame in data:
    print(frame)
    for face_id in data[frame]:
        a = data[frame][face_id]['age']
        b = data[frame][face_id]['gender']
        temp.append([a, b])
        print(temp)

        for i in k:
            face_data = [a, b]
            if not(i in face_data):
                xd.append(i)
                k.append(face_data)

print(xd)




