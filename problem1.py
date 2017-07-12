sum = 0
for j in range(1000):
    if (j % 5 == 0 or j % 3 == 0):
        sum = sum + j
print sum
