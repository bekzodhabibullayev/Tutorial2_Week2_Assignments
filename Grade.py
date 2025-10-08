student_name = input("What is your name: ")
gpa = float(input("What is your gpa: "))
credit_hours = int(input("How many hours of credits you have? : "))
if gpa>=3.5 and credit_hours>=12:
 print ("Acceptible")
else:
 print(f"Credit hours {student_name} has: {credit_hours};")
print(f"Student's gpa: you need {3.5-gpa} points;")

