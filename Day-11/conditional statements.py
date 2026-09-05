budget = int(input())
if budget > 10000:
    print("Cloud Hosting")
elif budget > 5000:
    print("Business Hosting")
elif budget > 2000:
    print("Premium Hosting")
else:
    print("Single Hosting")            