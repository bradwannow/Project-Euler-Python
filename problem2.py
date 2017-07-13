fib = 0
a = 0
b = 1
temp = 0
while b <= 4000000:
    temp = a + b
    a = b
    b = temp
    if b % 2 == 0:
      fib = fib + b
print (fib)
    
    
