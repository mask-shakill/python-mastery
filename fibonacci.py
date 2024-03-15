def fibonacci(n):
    init_array = [0,1]
    finalize = 0
    for i in range(n-2):
        finalize = init_array[-1] + init_array[-2]
        init_array.append(finalize)

    print(init_array)

n = int(input("enter your number of sequence : "))
fibonacci(n)  
    