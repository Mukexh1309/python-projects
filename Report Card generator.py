def get_mark(subject):
    mark = int(input(f"Enter your {subject} Mark: "))

    while mark < 0 or mark > 100:
        print("Marks are Invalid")
        mark = int(input(f"Enter your {subject} Mark again: "))

    return mark

Name = str(input("Enter Student Name:"))
Reg_No = int(input("Enter Reg No:"))

Mathematics = get_mark("Mathematics")
Physics = get_mark("Physics")
Chemistry = get_mark("Chemistry")
Computer_Science = get_mark("Computer Science")
English = get_mark("English")
Tamil = get_mark("Tamil")

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
