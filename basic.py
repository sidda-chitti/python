'''
#sum of numbers

n=int(input())
s=0
for i in range(1,n+1):
    s+=i
print(s)

#sum of natural numbers

n=int(input())
s=(n*(n+1)//2)
print(s)


#sum of numbers in a given range

a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    s+=i
print(s)


#greatest number

a,b,c=map(int,input().split())
print(max(a,b,c))



a,b,c=map(int,input().split())
max=0
if a>b:
    if a>c:
        max=a
    elif c>a:
        max=c
elif b>a:
    if b>c:
        max=b
    elif c>b:
        max=c
print(max)

        

a,b,c = map(int,input().split())
if a==b==c:
    print("equal")
elif a>b & a>c:
    print(a)
elif b>a & b>c:
    print(b)
else:
    print(c)


19
#leap year or not

n=int(input())
if (n%400==0) or ((n%4==0) and (n%100!=0)):
    print("leap")
else:
    print("not leap")


#prime or not

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")


less time taken

n=int(input())
flag=0
for i in range(2,n//2+1):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")




#prime numbers in a given range

low,high=map(int,input().split())
p=[]
for i in range(low,high+1):
    flag=0
    if i<2:
        continue
    if i==2:
        p.append(2)
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        p.append(i)
print(p)

            
   
#sum of digits in a number

n=int(input())
s=0
for i in str(n):
    s+=int(i)
print(s)



n=int(input())
s=0
while n>0:
    digit=n%10
    s+=digit
    n=n//10
print(s)

    

#reverse a number

n=int(input())
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print(rev)


    
n=int(input())
s=str(n)
print(s[::-1])




#palindrome

n=int(input())
temp=n
rev=0
while temp>0:
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
if n==rev:
    print("palindrome number")
else:
    print("not palindrome")




s=input()
rev=''.join(reversed(s))
if s==rev:
    print("palindrome")
else:
    print("not palindrome")




n=int(input())
temp=n
p=len(str(temp))
s=0
for i in range(p):
    digit=temp%10
    temp=temp//10
    s+=pow(digit,p)
if n==s:
    print("armstrong")
else:
    print("not armstrong")
    


#fibbinocci

n=int(input())
a,b=0,1
print(a,b, end=' ')
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c, end=' ')
print()

7 

#factorial
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return(n*factorial(n-1))

n=int(input())
print(factorial(n))



n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)



#power of a number

num,power=map(int,input().split())
print(pow(num,power))



num,power=map(int,input().split())
mul=1
for i in range(power):
    mul*=num
print(mul)



#factors of a number

n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(*l)
        


n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(s)



# perfect square

import math
n=int(input())
sq=int(math.sqrt(n))
if n==sq*sq:
    print("perfect")
else:
    print("not perfect")
    


import math
n=int(input())
if (math.floor(math.sqrt(n)))==(math.ceil(math.sqrt(n))):
    print("perfect")
else:
    print("not perfect")

    

#automorphic
#5-5^2=25 - ends with 5

n=int(input())
a=str(n)
sq=n*n
b=str(sq)

if b.endswith(a):
    print("automorphic")
else:
    print("not")


#by using modulo operator

n=int(input())
sq=n*n
mod=pow(10,len(str(n)))
if sq%mod == n:
    print("autom")
else:
    print("not")



#harshed

n=int(input())
temp=n
s=0
while temp>0:
    digit=temp%10
    s+=digit
    temp=temp//10
if n%s==0:
    print("harshed")
else:
    print("not")



#abundant number or not

n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s>n:
    print("abundant")
else:
    print("not")




n=int(input())
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
if s>n:
    print("abundant")
else:
    print("not")




a,b=map(int,input().split())
s1=0
s2=0
for i in range(1,a//2+1):
    if a%i==0:
        s1+=i
for i in range(1,b//2+1):
    if b%i==0:
        s2+=i
if (s1/a==s2/b):
    print("friendly pair")
else:
    print("not")
        

'''






