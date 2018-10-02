def printfiz(i):
    if (i % 3) == 0:
        result = "fizz"
        if (i % 5) == 0:
            result = "fizzbuzz"
        else:
            if (i % 5) == 0:
                result = "buzz"
    else:
        result = str(i)
    return result
    
for i in range(1, 101):
    print(printfiz(i))