fname = input("Enter file:")
if len(fname) < 1:
    fname = "regex_sum_42.txt"

with open(fname, 'r') as file:
    file_content = file.read()

nums = re.findall(r'[0-9]+', file_content)
print(sum([int(x) for x in nums]))