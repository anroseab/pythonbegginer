employee={
    'name':'john',
    'age':39,
    'salary':10000,
    "Destination": 'Manager'

}
print(employee)
print(employee['name'],employee['age'])

for i in employee:
    print(i)

for i in employee.values():
    print(i)

for key in employee:
    print(key  + ':' + str(employee[key ]))