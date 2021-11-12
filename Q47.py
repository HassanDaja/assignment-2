passwd=input("Enter The password:")
numbers=0
upper=0
lower=0
letter=[]
if 6<=len(passwd)<=20:
    for x in passwd:
        letter.append(x)
    for x in letter:
        if x.isdigit():
            numbers+=1
        elif x.isupper():
            upper+=1
        elif x.islower():
            lower+=1
    if lower>0 and upper>0 and numbers>0:
        print("valid")

    else:
        print("not valid")
else:
    print("The password length should be between 6 and 20")