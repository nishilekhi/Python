
medical=(input("Do you have a medical condition?(Y/N)")).strip().upper()
if medical == 'Y':
    print("You can take the test.")
else:
    absent = int(input("Enter the attendaance of student: "))

    if absent >= 75:
        print("Allowed")
    else:
        print("Not allowed")