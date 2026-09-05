fa = eval(input("Follows Account: "))
cf = eval(input("close Friend: "))
if fa:
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")

reg = input("Registered (yes/no): ")

if reg.lower() == "yes":
    fee = input("Entry fee paid? (yes/no): ")
    if fee.lower() == "yes":
        print("Tournament Entry confirmed")
    else:
        print("Entry fee is pending")
else:
    print("Registration required")

la=eval(input("link active: "))
pd=eval(input("permission denied: "))
if la:
    if pd:
        print("file open sucessfully")
    else:
        print("Invalid file link")