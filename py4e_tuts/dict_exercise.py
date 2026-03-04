fname = input("Enter file:")
if len(fname) < 1:
    name = "mbox-short.txt"
fh = open(fname)
email_count_dict = dict()
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    email = words[1]
    email_count_dict[email] =  email_count_dict.get(email,0) + 1

count = 0
max_count_email = ""
for key, val in email_count_dict.items():
    if val > count:
        max_count_email = key
        count = val
        
print(max_count_email, count)