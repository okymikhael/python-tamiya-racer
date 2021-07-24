import random
import string

def takeSecond(elem):
    return elem[1]

step = 0
five_fastest = []
three_fastest = []
tamiya_and_eye = list((list(string.ascii_uppercase)[x], random.randrange(10, 100, 5)) for x in range(0, 25))

print("Tamiya Eyes")
print(tamiya_and_eye)
print("End Tamiya Eyes\n")

print("----Race Begin----")
for i in range(0, len(tamiya_and_eye)):
    if tamiya_and_eye[i] not in three_fastest:
        three_fastest.append(tamiya_and_eye[i]) 
    if(len(three_fastest) < 5):
        continue
    else:
        three_fastest.sort(key=takeSecond)
        three_fastest = three_fastest[:3]
        step+=1

print("Three fastest tamiya:", three_fastest)
print("Much step for finding 3 fastest tamiya: ", step, "\n")
print("Removing 3 fastest tamiya for finding another 2 tamiya\n")

for i in three_fastest:
    tamiya_and_eye.remove(i)
# print(tamiya_and_eye)
        
for i in range(0, len(tamiya_and_eye)):
    if tamiya_and_eye[i] not in five_fastest:
        five_fastest.append(tamiya_and_eye[i]) 
    if(len(five_fastest) < 5):
        continue
    else:
        five_fastest.sort(key=takeSecond)
        five_fastest = five_fastest[:2]
        step+=1
        
five_fastest.sort(key=takeSecond)
step+=1

five_fastest = three_fastest + five_fastest[:2]
print("Five fastest tamiya:", five_fastest)
print("Much step for finding 5 fastest tamiya: ", step)
print("----End Race----")