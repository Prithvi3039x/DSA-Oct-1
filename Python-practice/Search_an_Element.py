arr = []
total = int(input("Entere the total number of elements: "))
print("Enter elements: ")
for i in range(total):
    num = int(input())
    arr.append(num)

search = int(input("Enter a number to search: "))

isPresent = False

for i in range(len(arr)):
    if arr[i] == search:
        isPresent = True
        break


if isPresent:
    print(f"{search} is present at {i+1} position.")
else:
    print(f"{search} is not present.")
