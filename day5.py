#write your code below  this row

for numbrr in range(1, 101):
    if numbrr % 3 == 0 and numbrr % 5 == 0:
        print("fizzbuzz")
    elif numbrr % 3 == 0:
        print("fizz")
    elif numbrr % 5 == 0:
        print("bizz")
    else:
        print(numbrr)
