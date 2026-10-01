arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)
new_arr = []

for i in range(len(arr)):
    if arr[i] != 0:
        new_arr.append(arr[i])

for i in range(len(arr)):
    if arr[i] == 0:
        new_arr.append(arr[i])



print(new_arr)
