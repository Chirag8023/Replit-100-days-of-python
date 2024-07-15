print("Let's check your grade on your test!")
print()

sub_name = input("Enter the name of the subject: ")
score = int(input("Enter your score: "))
percentage = round((score / 100) * 100, 2)

if percentage >= 90:
  grade = 'A+'
elif percentage >= 80 and percentage < 90:
  grade = 'A'
elif percentage >= 70 and percentage < 80:
  grade = 'B'
elif percentage >= 60 and percentage <70:
  grade = 'C'
elif percentage >= 40 and percentage < 60:
  grade = 'D'
else:
  grade = 'F'


print(f"\nFor the {sub_name} test you got : {percentage}%.")
print(f"Your grade is {grade}")