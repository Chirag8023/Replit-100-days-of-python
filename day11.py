print("Leap Year and Seconds calculator")
print()
year = int (input("Enter the year here: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) and (year % 100 == 0): 
  secondsInLeapYear = 60 * 60 * 24 * 366
  print("This is a Leap Year with:", secondsInLeapYear,"seconds")
else:
  secondsInStandardYear = 60 * 60 * 24 * 365 
  print("This is a Non-Leap Year with:",secondsInStandardYear,"seconds")




