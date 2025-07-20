min=30
student=float(input("enter ur marks"))
if student>=min:
    print("Eligible")
elif student>=25:
    print("Waiting list")
else:
    print("Not eligible")