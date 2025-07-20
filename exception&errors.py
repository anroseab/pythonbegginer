try:
    a=int(input("~"))
except Exception:
    print("User error")

try:
    a=int(input("~"))
except Exception as error:
    print("User error","Error:" +str(error))

try:
   print("opend")
   a=int(input("~"))
except ValueError:
    print("Invalid user inpput")
except TypeError:
    print("Type error")
except KeyboardInterrupt:
    print("Keyword Interrupted")
finally:
    print("closed")