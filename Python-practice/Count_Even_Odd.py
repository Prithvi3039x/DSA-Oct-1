arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are: ",arr)

count_even, count_odd = 0,0

for i in arr:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Total even numbers: ",count_even)
print("Total odd numbers: ",count_odd)
    