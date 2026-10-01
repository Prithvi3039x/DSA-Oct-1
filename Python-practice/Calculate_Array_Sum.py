arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)

sum = 0
for i in arr:
    sum+=i

print("The sum of numbers is: ",sum)
