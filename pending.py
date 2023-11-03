
        
  

##project:BMI calucator 
weight=float(input("enter the  weight in kg"))
height=float(input("enter the height in meter"))
BMI=weight/height**2
print(BMI)
if BMI< 18.25:
    print("under weight")
elif BMI< 50:
    print("healthy weight")
else:
    print("over weight")



