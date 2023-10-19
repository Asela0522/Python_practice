# In this code user can enter the marks and student name 
# After user can get User name and grade
Number_Of_Students=int(input("Enter The Number Of Students:"))
def Marks():
  Name=input("Enter the student name:")
  Name_First_Charactor=Name[0]
  Name_First_Charactor01=Name_First_Charactor.upper()
  Name_Last_Charactors=Name[1:]
  Full_Name=Name_First_Charactor01+Name_Last_Charactors
  marks=eval(input("Enter the student marks:"))

  if marks<0 or marks>100:# check the marks is valid or not
    return "Invalid Marks\n"
  # iin this area find the grade of the student
  elif marks<35:
    return f"Hi {Full_Name}\nYour Grage is W\n"
  elif marks<55:
    return f"Hi {Full_Name}\nYour Grage is S\n"
  elif marks<65:
    return f"Hi {Full_Name}\nYour Grage is C\n" 
  elif marks<75:
    return f"Hi {Full_Name}\nYour Grage is B\n"
  else:
    return f"Hi {Full_Name}\nYour Grage is A\n"    
        
for i in range(0,Number_Of_Students):
   print(Marks())# call The Marks() funtion