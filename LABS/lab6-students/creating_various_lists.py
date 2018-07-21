import random
n=int(input("Enter a positive even integer for the size of the list?" ))
#list with 0s
a = [0 for i in range(n)] #V1
#a = [0] * n V2
#random numbers between 1 and 100.
b = [random.randint(1,100) for i in range(n)] #v1


#alias
c = b
#set first half of c to 0
c = [0 for i in range(len(c)//2)] + b[len(c)//2:]
     
print(b)
print(c)

#copy b into d
d = [b[i] for i in range(len(l))] #v1
d = b[:] #v2

#e
e = [b[i] for i in range(0,len(b),2)]
