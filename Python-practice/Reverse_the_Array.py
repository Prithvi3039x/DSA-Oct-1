arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)

print("Reversed array :", arr[::-1])