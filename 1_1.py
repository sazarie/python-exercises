start = 2000
while start % 7 != 0 or start % 5 == 0:
    start += 1
print(start, end="")
for x in range(start+1, 3201):
    if x % 7 == 0 and not x % 5 == 0:
        print(",", x, end='', sep="")
