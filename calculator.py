valid=True
while True:
    first_number=input("Enter first number:")
    if first_number=="q":
        break
    try:
        first_number=float(first_number)
    except ValueError:
        print("please enter number!")
        continue

    operator=input("Enter the operator(+,-,*,/):")
    if operator not in ["+" , "-" , "*" , "/"]:
        print("Please enter a correct operator!")
        continue

    try:
        second_number=float(input("Enter second number:"))
    except ValueError:
        print("please enter number!")
        continue

    if operator=="+":
        answer=first_number+second_number
    elif operator=="-":
        answer=first_number-second_number
    elif operator=="*":
        answer=first_number*second_number
    elif operator=="/":
        if second_number==0:
            valid=False
            print("A number cannot be divided by 0")
        else: 
            answer=first_number/second_number

    if valid==True:
        print("Answer is:",answer)



