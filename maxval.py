import random
def maxval(list):
    list.sort()
    maxvalue = list[len(list)-1]
    print("Sorted list: ", list)
    print("\n")
    return maxvalue

list = []
for i in range(100):
    list.append(random.randint(0,1000))
print("Original list: ", list)

print("\n")
print("The max value of this list is ", maxval(list))
