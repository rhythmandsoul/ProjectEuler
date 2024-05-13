# Question: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

list_e=list() # Create new list
a,b=1,2 # Must have a trigger
list_e.append(2) # I don't need 1
c=0
print(a) # This is for control
print(b) # This is optional, just for control
while b<3500000: # This is a mistake. I put four million but loop works one more time and generate number bigger than foru million
    # for range(x) is about the loop time i guess. 
    # I just figurated out that the last necessary number is 3524578.
    # This is a temp and primitive solution. Will solve rational way but I must learn from mistakes.
    c=a+b # First sum is not in loop, it is a trigger! a=1 b =2 c= 3
    print(c)
    if c%2==0: # If c can be divided by two, append to list. 
        liste.append(c) # I know I can make without list but I wanted to practise lists :))
    a=b+c # Loop continues
    print(a)
    if a%2==0: 
        liste.append(a)
    b=a+c 
    print(b)
    if b%2==0: 
        liste.append(b)
print("*"*18)
print(list_e)
sum=0
for i in range(0,len(list_e)): #Listenin sayısı kadar tur dönecek bir döngü yazıyorum
    sum+=int(list_e[i]) #loop for sum in members of list_e
print(toplam)



############################# Official Project Euler Solution: ############################################

