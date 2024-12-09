name=input("Enter your Name: ")
English = float(input("English Grade: "))
Math = float(input("Math Grade:"))
Filipino = float(input("Filipino Grade: "))
Science = float(input("Science Grade: "))
average = English + Math + Filipino + Science
total_average = average/4
if total_average < 70:
    print(f"You Failed, you had an average of {total_average}")
else:
    print("You Passed!")
    print(f"You had an average of {total_average}")