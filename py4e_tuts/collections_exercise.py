fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    for word in line.split():
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)