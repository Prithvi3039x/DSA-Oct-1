arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)

max_num = arr[0]
min_num = arr[0]

for i in arr:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i

print("Maximum number is: ",max_num)
print("Minimum number is: ",min_num)