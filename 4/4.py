import re

f = open("passwords.txt", "w")
passwords = []

# Part One
count = 0 
f.write("# PART ONE PASSWORDS\n")
for N in range(136818, 685980):
    n = str(N)
    flag = 0
    if re.match(r"\d*(\d)\1\d*", n):
        flag = 1
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                flag = 0
                break
    
    if flag:
        f.write(n+"\n")
        passwords.append(n)
        count += 1

print("Part One Answer:", count)


        