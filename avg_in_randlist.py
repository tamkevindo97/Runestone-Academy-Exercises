import random

def average(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = sum/len(list)
    print("List = ", list)
    print("Sum = ", sum)
    print("Average = Sum divided by", len(list), "(Number of items in list)")
    print("Average = ", average)

list = []
def listsize(sz):
    for i in range(sz):
        list.append(random.randint(0,1000))

sz = int(input("Enter size of list: "))
listsize(sz)
average(list)
