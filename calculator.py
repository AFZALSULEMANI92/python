restart = 'true'
while restart == 'true':
     print('enter a')
     a=int(input())
     print('enter b')
     b=int(input())
     print('what you want to do ')
     c=input()
     if c =='+':
          print(a+b)
     elif c=='-':
          print(a-b) 
     elif c=='*' :     
          print(a*b) 
     elif c=='/' :     
          print(a*b)     
     d=input('restart again y/n')
     if d!='y':
         restart = false
          