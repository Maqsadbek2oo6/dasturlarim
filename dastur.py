for son in range(1, 50):
    if son%3==0 and son%5==0:
        print("FizzBuzz")    
    elif son%3==0:
        print("Fizz")
    elif son%5==0:
        print("Buzz")
    else:
        print(son)
