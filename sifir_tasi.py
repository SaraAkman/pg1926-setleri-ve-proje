x = int(input("Lütfen bir tam sayı giriniz: "))
y = int(input("Lütfen başka bir tam sayı daha giriniz: "))
z = int(input("Lütfen bir tam sayıdaha giriniz: "))
q = int(input("Lütfen bir tam sayı daha giriniz: "))
a = int(input("Lütfen bir tam sayı daha giriniz: "))
b = int(input("Lütfen başka bir tam sayı daha giriniz: "))
c = int(input("Lütfen başka bir tam sayı daha giriniz: "))
if (q==0) and (x==0):
  print(x,q,y,z,a,b,c)
elif (z==0)and (x==0):
  print(x,z,y,q,a,b,c)  
elif (y==0)and (x==0):
  print(x,y,z,q,a,b,c)   
elif (a==0)and (x==0):
  print(x,a,y,z,q,b,c) 
elif (b==0)and (x==0):
  print(x,b,y,z,q,a,c) 
elif (c==0)and (x==0):
  print(x,c,y,z,q,a,b)

elif (y==0)and (z==0):
  print(y,z,x,q,a,b,c)
elif (y==0)and (q==0):
  print(y,q,x,z,a,b,c)  
elif (y==0)and (a==0):
  print(y,a,x,z,q,b,c)
elif (y==0)and (b==0):
  print(y,b,x,z,q,a,c)
elif (y==0)and (c==0):
  print(y,c,x,z,q,a,b)

elif (z==0)and (q==0):
  print(z,q,x,y,a,b,c)
elif (z==0)and (a==0):
  print(z,a,x,y,q,b,c) 
elif (z==0)and (b==0):
  print(z,b,x,y,q,a,c) 
elif (z==0)and (c==0):
  print(z,c,x,y,q,a,b) 

elif (a==0)and (b==0):
  print(a,b,x,y,z,q,c) 
elif (a==0)and (c==0):
  print(a,c,x,y,z,q,b) 

elif (c==0)and (b==0):
  print(c,b,x,y,z,q,a) 

elif (q==0)and (b==0):
  print(q,b,z,a,x,c,y) 
elif (q==0)and (a==0):
  print(q,a,z,b,x,c,y) 
elif (q==0)and (c==0):
  print(q,c,z,a,x,b,y) 

elif (a==0)and (x==0)and (y==0) :
  print(x,a,y,z,q,b,c)    
elif (a==0)and (x==0)and (z==0) :
  print(x,a,z,y,q,b,c)  
elif (a==0)and (x==0)and (q==0) :
  print(x,a,q,y,z,b,c)  
elif (a==0)and (x==0)and (b==0) :
  print(x,a,b,y,z,q,c)
elif (a==0)and (x==0)and (c==0) :
  print(x,a,c,y,z,q,b)

elif (z==0)and (x==0)and (y==0) :
  print(x,z,y,q,a,b,c)
elif (q==0)and (x==0)and (y==0) :
  print(x,q,y,z,a,b,c)
elif (b==0)and (x==0)and (y==0) :
  print(x,b,y,q,a,z,c)
elif (c==0)and (x==0)and (y==0) :
  print(x,c,y,q,a,b,z)

elif (z==0)and (x==0)and (q==0) :
  print(x,z,q,y,a,b,c)
elif (z==0)and (x==0)and (b==0) :
  print(x,z,b,y,q,a,c)
elif (z==0)and (x==0)and (c==0) :
  print(x,z,c,y,q,a,b)

elif (x==0)and (q==0)and (b==0) :
  print(x,q,b,y,z,a,c)
elif (x==0)and (q==0)and (c==0) :
  print(x,q,c,y,z,a,b)
  
elif (x==0)and (b==0)and (c==0) :
  print(x,b,c,y,z,q,a)
elif (x==0)and (b==0)and (a==0) :
  print(x,b,a,y,z,q,c)

elif (y==0)and (z==0)and (q==0) :
  print(y,z,q,x,a,b,c)
elif (y==0)and (z==0)and (a==0) :
  print(y,z,a,x,q,b,c)
elif (y==0)and (z==0)and (b==0) :
  print(y,z,b,x,q,a,c)
elif (y==0)and (z==0)and (c==0) :
  print(y,z,c,x,q,a,b)

elif (y==0)and (q==0)and (a==0) :
  print(y,q,a,x,z,b,c)
elif (y==0)and (q==0)and (b==0) :
  print(y,q,b,x,z,a,c)
elif (y==0)and (q==0)and (c==0) :
  print(y,q,c,x,z,a,b)  

elif (a==0)and (y==0)and (b==0) :
  print(y,a,b,x,z,q,c)
elif (a==0)and (y==0)and (c==0) :
  print(y,a,c,x,z,q,b)
elif (b==0)and (y==0)and (c==0) :
  print(y,b,c,x,z,q,a)

elif (q==0)and (z==0)and (a==0) :
  print(a,z,q,x,y,b,c)
elif (q==0)and (z==0)and (b==0) :
  print(b,z,q,x,y,a,c)
elif (q==0)and (z==0)and (c==0) :
  print(c,z,q,x,y,a,b)

elif (q==0)and (b==0)and (a==0) :
  print(a,b,q,x,y,z,c)  
elif (q==0)and (c==0)and (a==0) :
  print(a,c,q,x,y,z,b)
elif (q==0)and (c==0)and (b==0) :
  print(b,c,q,x,y,z,a)

elif (z==0)and (c==0)and (b==0) :
  print(z,c,a,x,y,q,b)
elif (z==0)and (a==0) and (b==0) :
  print(z,b,a,x,y,q,c)
elif (z==0)and (a==0)and (c==0) :
  print(z,c,a,x,y,q,b)

elif (a==0)and (c==0)and (b==0) :
  print(b,c,a,x,y,z,q)

elif (x==0)and (y==0)and (z==0) and (q==0) :
  print(x,y,z,q,a,b,c)
elif (x==0)and (y==0)and (z==0) and (a==0) :
  print(x,y,z,a,q,b,c)
elif (x==0)and (y==0)and (z==0) and (b==0) :
  print(x,y,z,b,q,a,c)
elif (x==0)and (y==0)and (z==0) and (c==0) :
  print(x,y,z,c,q,a,b)

elif (x==0)and (y==0)and (q==0) and (a==0) :
  print(x,y,z,a,q,b,c)
elif (x==0)and (y==0)and (q==0) and (b==0) :
  print(x,y,z,b,q,a,c)
elif (x==0)and (y==0)and (q==0) and (c==0) :
  print(x,y,z,c,q,a,b)

elif (x==0)and (y==0)and (b==0) and (c==0) :
  print(x,y,b,c,z,q,a)
elif (x==0)and (y==0)and (a==0) and (c==0) :
  print(x,y,a,c,z,q,b)
elif (x==0)and (y==0)and (a==0) and (b==0) :
  print(x,y,a,b,z,q,)

elif (x==0) and (z==0) and (q==0) and (a==0):
  print(x,z,a,q,y,b,c)
elif (x==0) and (z==0) and (q==0) and (b==0):
  print(x,z,b,q,y,a,c)
elif (x==0) and (z==0) and (q==0) and (c==0):
  print(x,z,c,q,y,a,b)

elif (x==0) and (z==0) and (a==0)and (b==0):
  print(x,z,a,b,y,q,c)
elif (x==0) and (z==0) and (a==0)and (c==0):
  print(x,z,a,c,y,q,b)
elif (x==0) and (z==0) and (c==0)and (b==0):
  print(x,z,b,c,y,q,a)

elif (x==0) and (q==0) and (a==0)and (b==0):
  print(x,q,a,b,y,z,c)
elif (x==0) and (q==0) and (a==0)and (c==0):
  print(x,q,a,c,y,z,b)
elif (x==0) and (q==0) and (c==0)and (b==0):
  print(x,q,b,c,y,z,a)

elif (x==0) and (c==0) and (a==0)and (b==0):
  print(x,c,a,b,y,z,q)

elif (y==0) and (z==0) and (q==0) and (a==0):
  print(y,z,a,q,x,b,c)
elif (y==0) and (z==0) and (q==0) and (b==0):
  print(y,z,b,q,x,a,c)
elif (y==0) and (z==0) and (q==0) and (c==0):
  print(y,z,c,q,x,a,b)

elif (y==0) and (z==0) and (a==0)and (b==0):
  print(y,z,a,b,x,q,c)
elif (y==0) and (z==0) and (a==0)and (c==0):
  print(y,z,a,c,x,q,b)
elif (y==0) and (z==0) and (c==0)and (b==0):
  print(y,z,b,c,x,q,a)

elif (y==0) and (q==0) and (a==0)and (b==0):
  print(y,q,a,b,x,z,c)
elif (y==0) and (q==0) and (a==0)and (c==0):
  print(y,q,a,c,x,z,b)
elif (y==0) and (q==0) and (c==0)and (b==0):
  print(y,q,b,c,x,z,a)

elif (y==0) and (c==0) and (a==0)and (b==0):
  print(y,c,a,b,x,z,q)

elif (z==0) and (q==0) and (a==0)and (b==0):
  print(z,q,a,b,x,y,c)
elif (z==0) and (q==0) and (a==0)and (c==0):
  print(z,q,a,c,x,y,b)
elif (z==0) and (q==0) and (c==0)and (b==0):
  print(z,q,b,c,x,y,a)

elif (z==0) and (c==0) and (a==0)and (b==0):
  print(z,c,a,b,x,y,q)

elif (q==0) and (c==0) and (a==0)and (b==0):
  print(q,c,a,b,x,y,z)

elif (x==0)and (y==0)and (z==0) and (q==0) and (a==0) :
  print(x,y,z,q,a,b,c)
elif (x==0)and (y==0)and (z==0) and (q==0) and (b==0) :
  print(x,y,z,q,b,a,c)
elif (x==0)and (y==0)and (z==0) and (q==0) and (c==0) :
  print(x,y,z,q,c,a,b)

elif (x==0)and (y==0)and (z==0) and (a==0) and (b==0) :
  print(x,y,z,a,b,q,c)
elif (x==0)and (y==0)and (z==0) and (a==0) and (c==0) :
  print(x,y,z,a,c,q,b)
elif (x==0)and (y==0)and (z==0) and (c==0) and (b==0) :
  print(x,y,z,c,b,q,a)

elif (x==0)and (y==0)and (q==0) and (a==0) and (b==0) :
  print(x,y,q,a,b,z,c)
elif (x==0)and (y==0)and (q==0) and (a==0) and (c==0) :
  print(x,y,q,a,c,z,b)
elif (x==0)and (y==0)and (q==0) and (c==0) and (b==0) :
  print(x,y,q,c,b,z,a)

elif (x==0)and (y==0)and (c==0) and (a==0) and (b==0) :
  print(x,y,c,a,b,z,q)

elif (x==0)and (z==0)and (q==0) and (a==0) and (b==0) :
  print(x,z,q,a,b,y,c)
elif (x==0)and (z==0)and (q==0) and (a==0) and (c==0) :
  print(x,z,q,a,c,y,b)
elif (x==0)and (z==0)and (q==0) and (c==0) and (b==0) :
  print(x,z,q,c,b,y,a)

elif (x==0)and (z==0)and (c==0) and (a==0) and (b==0) :
  print(x,z,c,a,b,y,q)

elif (x==0)and (q==0)and (c==0) and (a==0) and (b==0) :
  print(x,q,c,a,b,y,z)

elif (y==0)and (z==0)and (q==0) and (a==0) and (b==0) :
  print(y,z,q,a,b,x,c)
elif (y==0)and (z==0)and (q==0) and (a==0) and (c==0) :
  print(y,z,q,a,c,x,b)
elif (y==0)and (z==0)and (q==0) and (c==0) and (b==0) :
  print(y,z,q,c,b,x,a)

elif (y==0)and (z==0)and (c==0) and (a==0) and (b==0) :
  print(y,z,c,a,b,x,q)

elif (y==0)and (q==0)and (c==0) and (a==0) and (b==0) :
  print(y,q,c,a,b,x,z)

elif (z==0)and (q==0)and (c==0) and (a==0) and (b==0) :
  print(z,q,c,a,b,x,y)

elif (x==0)and (y==0)and (z==0) and (q==0) and (a==0) and (b==0) :
  print(x,y,z,q,a,b,c)
elif (x==0)and (y==0)and (z==0) and (q==0) and (a==0) and (c==0) :
  print(x,y,z,q,a,c,b)
elif (x==0)and (y==0)and (z==0) and (q==0) and (c==0) and (b==0) :
  print(x,y,z,q,c,b,a)

elif (x==0)and (y==0)and (z==0) and (a==0) and (c==0) and (b==0) :
  print(x,y,z,a,c,b,q)

elif (x==0)and (y==0)and (a==0) and (q==0) and (c==0) and (b==0) :
  print(x,y,q,c,b,a,z)
elif (x==0)and (z==0)and (a==0) and (q==0) and (c==0) and (b==0) :
  print(x,z,q,c,b,a,y)
elif (z==0)and (y==0)and (a==0) and (q==0) and (c==0) and (b==0) :
  print(z,y,q,c,b,a,x)
else:
  print(x,y,z,q,a,b,c)

