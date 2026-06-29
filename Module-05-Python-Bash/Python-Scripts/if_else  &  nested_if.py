marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

else:
    print("Fail")


# Output
Grade B



#nested-if
  
  age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Not Eligible")


# Output
Eligible to Vote
