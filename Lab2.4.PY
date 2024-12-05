name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")
marks = int(input("Enter marks secured in Mathematics (out of 100): "))

if marks >= 90:
    grade_point = 10
    remark = "OUTSTANDING"
elif marks >= 80:
    grade_point = 9
    remark = "VERY GOOD"
elif marks >= 70:
    grade_point = 8
    remark = "GOOD"
elif marks >= 60:
    grade_point = 7
    remark = "AVERAGE"
elif marks >= 50:
    grade_point = 6
    remark = "PASS"
else:
    grade_point = 0
    remark = "FAIL"

print("\nStudent Details:")
print("Name:", name)
print("Roll Number:", roll_number)
print("Marks:", marks)
print("Grade Point:", grade_point)
print("Remark:", remark)
