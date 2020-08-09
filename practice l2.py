a=[5,7,8,9,'ok','kot','loc']
b=[]
c=[]
for i in a:
     if (type(i))==int:
          b.append(i)
     else:
          c.append(i)     
print(b)
print(c)