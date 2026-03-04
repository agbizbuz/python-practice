def spam_value(spam_txt):
    spam_txt.strip()
    indx = spam_txt.find(':')
    num = spam_txt[indx + 1:-1]
    return float(num)
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num_lines = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    tot = tot + spam_value(line)
    num_lines = num_lines + 1
print("Average spam confidence:", (tot/num_lines))

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
