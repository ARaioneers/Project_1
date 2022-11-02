def factorial(a):
    print("***********")
    f=1
    if a>=0:
        for i in range(1,a+1):
            f=f*i
            print(f"Factorial of Number {a} is = ",f)
    else:
        print("Factorial is not found")
        factorial()
        
factorial(5)