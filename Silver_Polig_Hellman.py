import math
from collections import Counter
import numpy as np


def simpleform(p):
    kanon=[]
    q=p-1
    while True:
        for x in xrange(2, int(math.sqrt(q))+2):
           if (is_prime(q)):
               kanon.append(q)
              # print q
               q = 1
               break
           elif(q%x ==0 & is_prime(x)):
               q=q/x
            #   print x , q
               kanon.append(x)
               break
        if (q == 1):
            break
    last=Counter(kanon)
    print last
    return last

def is_prime(a):
    return all(a % i for i in xrange(2, int(math.sqrt(a))+1))

def chain(a,b,i):
    if (i==0) :
        return a
    else:
        print (a-a%b)/b
        i=i-1
        return chain(b,a%b,i)

def SPHalgo(a,b,p):
    prep = simpleform(p)
    table=dict()
    for key in prep:
        for x in range(0,key):
            w= pow(a,(x*(p-1)/key),p)
            if key in table:
                table[key].append([x,w])
            else:
                table[key]=[[x,w]]
            print key,x,w
#    for key in table:
#        for x in range(0,)
    return table
#print simpleform(37)
#print is_prime(3)
#print SPHalgo(5,13,109)
chain(4633,1921,4)

