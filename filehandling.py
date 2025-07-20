with open('filehanding.txt','r') as file:
    data=file.read()
    print(data)

with open('filehanding.txt','r') as file:
    data=file.readlines(2)
    print(data)