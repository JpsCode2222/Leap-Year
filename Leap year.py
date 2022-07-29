Y=int(input("Enter Year: "))
if Y % 100 == 0 and Y % 400 == 0:
      print("Entered Year is leap Year")
elif Y % 100 != 0 and Y % 4 == 0:
    print("Entered Year is leap Year")
else:
    print("Entered year is not leap year")
