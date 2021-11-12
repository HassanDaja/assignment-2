def discount():
    discount_percent=5/100
    product_price=int(input("product price:"))

    member=False
    x=True
    while x:
        print("Enter number")
        is_member=int(input("1.Yes//2.No:"))
        if is_member==1:
            member=True
            x=False
        elif is_member==2:
            member=False
            x = False

        else:
            continue
        if member==True:
            discount_percent+=10/100
            discount_amount=product_price*(discount_percent)
            product_price-=discount_amount
        else:
            discount_amount = product_price * (discount_percent)
            product_price -= discount_amount
    return int(product_price)







