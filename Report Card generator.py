Name = str(input("Enter Student Name:"))
Reg_No = int(input("Enter Reg No:"))

Mathematics = int(input("Enter your Mathematics Mark:"))
while Mathematics < 0 or Mathematics > 100:
    print("Marks are Invalid")
    Mathematics = int(input("Enter your Mathematics Mark again: "))

Physics = int(input("Enter your Physics Mark:"))
while Physics < 0 or Physics > 100:
    print("Marks are Invalid")
    Physics = int(input("Enter your Physics Mark again: "))

Chemistry = int(input("Enter your Chemistry Mark:"))
while Chemistry < 0 or Chemistry > 100:
    print("Marks are Invalid")
    Chemistry = int(input("Enter your Chemistry Mark again: "))

Computer_Science = int(input("Enter your Computer Science Mark:"))
while Computer_Science < 0 or Computer_Science > 100:
    print("Marks are Invalid")
    Computer_Science = int(input("Enter your Computer Science Mark again: "))
    
English = int(input("Enter your English Mark:"))
while English < 0 or English > 100:
    print("Marks are Invalid")
    English = int(input("Enter your English Mark again: "))
    
Tamil = int(input("Enter your Tamil Mark:"))
while Tamil < 0 or Tamil > 100:
    print("Marks are Invalid")
    Tamil = int(input("Enter your Tamil Mark again: "))

Total = Mathematics + Physics + Chemistry + Computer_Science + English + Tamil
Percentage = Total / 600*100

if Percentage >= 90:
    Grade = "A+"
elif Percentage >= 80:
    Grade = "A"
elif Percentage >= 70:
    Grade = "B"
elif Percentage >= 60:
    Grade = "C"
else:
    Grade = "D"

if Mathematics >= 35 and Physics >= 35 and Chemistry >= 35 and Computer_Science >= 35 and English >= 35 and Tamil >= 35:
    Result = "PASS"
else:
    Result = "FAIL"
    
     
print("========================================")
print("          STUDENT REPORT CARD")
print("========================================")
print(f"Student Name : {Name}")
print(f"Reg No       : {Reg_No}")
print("----------------------------------------")
print(f"Mathematics  : {Mathematics}")
print(f"Physics      : {Physics}")
print(f"Chemistry    : {Chemistry}")
print(f"Computer Sci : {Computer_Science}")
print(f"English      : {English}")
print(f"Tamil        : {Tamil}")
print("----------------------------------------")
print(f"Total        : {Total} / 600")
print(f"Percentage   : {Percentage:.2f}%")
print(f"Grade        : {Grade}")
print(f"Result       : {Result}")
print("========================================")
