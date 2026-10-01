arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)