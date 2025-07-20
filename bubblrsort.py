
li=[8,3,1,4]
print(li)
leng=len(li)
for i in range (leng):
    for j in range(0,leng-i-1):
       if li[j]>li[j+1]:
          li[j],li[j+1]=li[j+1],li[j]
print(li)
           
