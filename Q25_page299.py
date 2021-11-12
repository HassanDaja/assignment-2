def digit_count(x):
    zeroes=0
    even=0
    odd=0

    z=str(x).split(".")
    if len(z)>1:
        for x in z[1]:
            if x=="0":
                zeroes+=1
            elif x=="1" or x=="3" or x=="5" or x=="7" or x=="9":
                odd+=1
            elif x=="2" or x=="4" or x=="6" or x=="8":
                even+=1

    return even, odd, zeroes






