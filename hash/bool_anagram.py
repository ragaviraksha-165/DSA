s1=input("enter s1: ") #geeks
s2=input("enter s2: ") #skeeg

def bool_anagram(s1,s2):
    s1="".join(sorted(s1))
    s2="".join(sorted(s2))

    if s1==s2:
        print("True")
    else:
        print("False")

bool_anagram(s1,s2)
