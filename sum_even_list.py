def sumEven(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            sum = sum + lst[i]
    return sum


lst = []
moreInputs = True
count = 0

while moreInputs:
    lst.append(int(input("Add integer (999 to end): ")))
    if lst[count] == 999:
        lst.pop()
        moreInputs = False
    else:
        count = count + 1
print("List: ", lst)

print("Sum of even numbers = ", sumEven(lst))

input('Press ENTER to exit')