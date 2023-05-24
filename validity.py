l,u,p,s = 0, 0, 0, 0
r = "R@s1"
if (len(r) >= 4):
    for i in r:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            s+=1
        if (i == "@" or "i" == "$" or i == "_"):
            p+=1
        if (l>=1 and u>=1 and p>=1 and s>=1 and l+u+p+s == len(r)):
            print("valid input")
        else:
            print("invalid")
            