def palindrome(n):
    reversed_n = int(str(n)[::-1])
    if n == reversed_n:
        print("Palindrome")
    else:
        print("Not Palindrome")
        
n = int(input("Enter your Numbers : "))
palindrome(n)