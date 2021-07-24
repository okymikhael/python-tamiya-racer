import random
import string
import time

def takeSecond(elem):
    return elem[1]

step = 0
five_fastest = []
three_fastest = []
tamiya_and_eye = list((list(string.ascii_uppercase)[x], random.randrange(10, 100, 5)) for x in range(0, 25))

print("Tamiya Speed")
print(tamiya_and_eye, "\n")

print("Winner Selection: ")
for i in range(0, len(tamiya_and_eye)):
    if tamiya_and_eye[i] not in three_fastest:
        three_fastest.append(tamiya_and_eye[i]) 
    print(three_fastest)
    if(len(three_fastest) < 5):
        time.sleep(0.5)
    else:
        print("Racing...")
        print(three_fastest)
        three_fastest.sort(key=takeSecond)
        three_fastest = three_fastest[:3]
        step+=1

print("\nWe have 3 fastest tamiya:")
print(three_fastest)
print("Much step for finding 3 fastest tamiya:", step)
print("Removing 3 fastest tamiya for finding another 2 tamiya\n")

for i in three_fastest:
    tamiya_and_eye.remove(i)
# print(tamiya_and_eye)
        
time.sleep(2)
print("Test 2 Beginning in")
time.sleep(0.5)
print("3", end=" ")
time.sleep(0.5)
print("2", end=" ")
time.sleep(0.5)
print("1\n")
time.sleep(1)

for i in range(0, len(tamiya_and_eye)):
    if tamiya_and_eye[i] not in five_fastest:
        five_fastest.append(tamiya_and_eye[i]) 
    print(five_fastest)
    if(len(five_fastest) < 5):
        time.sleep(0.5)
    else:
        print("Racing...")
        print(five_fastest)
        five_fastest.sort(key=takeSecond)
        five_fastest = five_fastest[:2]
        step+=1
        
five_fastest.sort(key=takeSecond)
five_fastest = three_fastest + five_fastest[:2]
step+=1

print("Five fastest tamiya:", five_fastest)
print("Much step for finding 5 fastest tamiya:", step)
