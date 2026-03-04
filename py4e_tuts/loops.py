largest = None
smallest = None
nums = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        nums.append(int(num))
    except:
        print("Invalid input")

largest = smallest = nums[0]
for a_num in nums:
    if smallest > a_num:
        smallest = a_num
    if largest < a_num:
        largest = a_num

print("Maximum is", largest)
print("Minimum is", smallest)