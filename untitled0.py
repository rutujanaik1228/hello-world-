
salary=int(input("Enter Salary of the employee : "))
g=input("Enter gender of the employee : ")
gender=g.upper()
if (salary<10000):
    if (gender=='MALE'):
        print("Salary with bonus for the male employee is Rs. ", sal+(sal*0.07))
    elif (gender=='FEMALE'):
      print("Salary with bonus for the female employee is Rs. ", sal+(sal*0.12))
    else:
        print("Invalid input")             
else:
    if (gender=='MALE'):
        print("Salary with bonus for the male employee is Rs. ", sal+(sal*0.05))
    elif (gender=='FEMALE'):
      print("Salary with bonus for the female employee is Rs. ", sal+(sal*0.10))
    else:
        print("Invalid input")

