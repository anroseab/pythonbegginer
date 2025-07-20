try:
   a=int(input("one:"))
   b=int(input("two:"))
   print(a/b)
except ValueError:
   print("Invalid input")
except ZeroDivisionError:
   print("nothing can be divided by 0") 