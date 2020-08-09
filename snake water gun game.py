import random
let=['snake','water','gun']
print('what you choose: snake,water,gun')
i=0
b=0
c=0
while i<10:
  a=input()
  choice=random.choice(let)
  if a=='snake' and choice=='water':
    print('you win')
    b=b+1
  elif a=='snake' and choice=='gun':
    print('you loss')
    c=c+1
  elif a=='gun' and choice=='water':
    print('you loss')
    c=c+1
  elif a=='gun' and choice=='snake':
    print('you win')
    b=b+1
  elif a=='water' and choice=='snake':
    print('you loss')
    c=c+1
  elif a=='water' and choice=='gun':
    print('you win')
    b=b+1        
  elif a==choice:
    print('game draw')
  i=i+1
print('game won by computer',c)
print('game won by you',b)
if (b>c):
  print('you win')
else:
  print('computer win')  