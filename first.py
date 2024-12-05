name = input("What's your name: ")
age = int(input("What's your age: "))
place = input("Where do you live: ")
num = int(input("Mobile #: "))
height = float(input("What's your height please put in decimal: "))
print("Information Saved")
print("-----------------------------------")
print ("Name: "+str(name) +"\n"+ "Age: "+str(age) +"\n"+"Place: " +str(place) +"\n"+"Mobile #: " +str(num) + "\n"+"Height: "+ str(height))
if age <= 17:
    print("You are a minor")
elif age >= 50:
    print ("Old ass")
else:
    print("Your an adult")