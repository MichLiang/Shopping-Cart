user_input=input("Enter your subtotal: $")

if user_input!="":
    subtotal=float(user_input)
    if subtotal>=50:
        shipping=0
    else:
        shipping=15

    user_input=input("Enter a coupon code: ")
    coupon=user_input

    if coupon==("SAVE10"):
        discount=subtotal*0.10
    else:
        discount=subtotal*0

    print("Coupon discount: $",discount)


    print("Shipping cost: $"+str(shipping))
    total=subtotal + shipping-discount
    print("Your total comes to: $",total)

else:
    print("Please input a value")
    user_input=input("Enter your subtotal: $")


    if user_input!="":
        subtotal=float(user_input)
        if subtotal>=50:
            shipping=0
        else:
            shipping=15

        user_input=input("Enter a coupon code: ")
        coupon=user_input

        if coupon==("SAVE10"):
            discount=subtotal*0.10
        else:
            discount=subtotal*0

        print("Coupon discount: $",discount)


        print("Shipping cost: $"+str(shipping))
        total=subtotal + shipping-discount
        print("Your total comes to: $",total)

    else:
        print("Please input a value")


# comma vs str, comma only really works in print
# also there's a space before total cause of it

#investigate while loops!!
