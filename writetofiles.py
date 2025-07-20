userInput=input("enter ur msg that u wish to same")
with open('filehanding.txt','a') as file:
    file.write(userInput +'\n')