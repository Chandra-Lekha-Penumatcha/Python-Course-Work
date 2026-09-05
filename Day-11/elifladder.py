budget = int(input())
if budget > 10000:
    print("Cloud hosting")
elif budget > 5000:
    print("business hosting")
elif budget > 2000:
    print("premium hosting")
else:
    print("single hosting")