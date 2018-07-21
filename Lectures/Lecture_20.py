##def h(n):
##    print(1/n) #print 1/2
##
##def g(n):
##    h(n-1)#n = 3, send h(2)
##    print(n) # print 3
##def f(n):
##    g(n-1) #n = 4, send g(3)
##    print(n) # print 4
##
##n = 4
##f(n) #send f(4)

def silly_printer(n):
    if n == 0:
        print("Blast off!")
    else:     
        print(n)
        silly_printer(n-1)

def sp_iter(n):
    while True:
        print(n)
        n = n-1
