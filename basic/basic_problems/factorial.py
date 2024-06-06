
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num=int(input("enter any number : "))
print("Factorial of", num, "is:", factorial(num)) 



fact=1
for i in range(1,num+1):
    fact = fact*i

print(fact)