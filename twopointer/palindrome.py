while True:
    s=input("enter a string: ")
    temp=""

    for i in s:
        if i.isalnum():
            temp+=i.lower()

    if temp==temp[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
