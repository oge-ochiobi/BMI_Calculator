# create a bmi calculator # 
Name = input("Name: ")
Age = int(input("Age: "))
Gender = input("Gender: ")
Weight = int(input("Weight in Kg: "))
Height = float(input("Height in Metres: "))
BMI = round(Weight / (Height*Height), 2)
print("Your BMI is: ",BMI, "kg/m^2")
if BMI > 0:
      if (BMI <18.5):
         print("You are underweight")
      elif (BMI <= 25):
           print("You are of normal weight")
      elif (BMI <= 30):
           print("You are overweight")
      else:
           print("You are obese") 