def myfn():
    print("This is our fn")
myfn()

def better(string):
    for char in string:
        print(char)
better("hekko")

def better(string='your not send an parameter'):
    for char in string:
        print(char)
better()

def better(end1,string='your not send an parameter'):
    for char in string:
        print(char,end1)
better(1)