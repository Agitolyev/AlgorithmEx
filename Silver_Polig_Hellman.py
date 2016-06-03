import math
from collections import Counter

def euclidExt(a, b):

  assert a != 0 or b != 0
  a0, a1, b0, b1 = 1, 0, 0, 1
  while b != 0:
    q, r = divmod(a, b)
    a, b = b, r
    a0, a1, b0, b1 = b0, b1, a0 - q*b0, a1 - q*b1
  return (a, a0, a1)

def simpleform(p):
    kanon=[]
    q=p
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
    return last

def is_prime(a):
    return all(a % i for i in xrange(2, int(math.sqrt(a))+1))

#def chain(a,b,i):
#    if (i==0) :
#        return a
#    else:
##        print (a-a%b)/b
#        i=i-1
#        return chain(b,a%b,i)

def chain(num,x):
    print "Let`s find chain form of number:"
    chainform = []
    v=1
    u=int(math.floor(math.sqrt(num)))
    print "Start values are : \n v = " + str(v) + "\n u0 =" + str(u)
    chainform.append(int((math.floor(math.sqrt(num)))))
    print "Following ones counted by formula : \n \n v=(num-pow(u,2,num))/v\n \n a=(u0+u)/v \n \n  u=a*v-u"
    for x in range(0,x):
        #vx=v
        v=(num-pow(u,2,num))/v
        a=(chainform[0]+u)/v
        u=a*v-u
        print "v = " + str(v) + "\n a = " + str(a) + "\n u = " + str(u)
        chainform.append(a)
    chainform.append(num)
    return chainform
def evector(chainform):
    print "On this Sep we have to make table of chain form, elements Pn and pow2 of each Pn element \n"
    print "\n So  we get chain form of Sqrt(n):"
    print chainform
    print "\n P.S. Last element is number itself, it`s just easier for transfering it from func to func \n"
    p=[0,1]
    powP=[]
    e = []
    for x in range(0,len(chainform)-1):
        p.append((chainform[x]*p[x+1]+p[x])%chainform[-1])

    print p
    print
    for x in p:
        powP.append(pow(x,2,chainform[-1]))
    print powP
    powP.pop(0)
    powP.pop(0)
    print
    for x in powP:
       for key in simpleform(x):
           if key in e:
               continue
           else:e.append(key)
    e.sort()
    #matrix = []
    #matrix.append(e)
    eVectors = dict()
    simplefor = dict()
    for x in powP:
        eVectors[x]=[0]*len(e)
    for key in eVectors:
        simplefor = simpleform(key)
        for x in simplefor:
            eVectors.get(key)[e.index(x)]=simplefor.get(x)
    print e
    return eVectors

def SPHalgo(a,b,p):
    prep = simpleform(p-1)
    table=dict()
    for key in prep:
        for x in range(0,key):
            w= pow(a,(x*(p-1)/key),p)
            if key in table:
                table[key].append([x,w])
            else:
                table[key]=[[x,w]]
            print key,x,w

 #   for key in table:
 #       for x in range(0,table[key]):
 # a^(x[n]*(p-1)/q[i]) = (b*a^(-x0-x[n]*q[i])^(p-1)/(q[i]^n+1) n=  0,1, ...
    return table

def find(x):
    while x%9!=7:
        x+=8
    return x
def show(x):
    for key in x :
        print str(x.get(key)) + "  "+str(key)


#print simpleform(73-1)
#print SPHalgo(5,34,73)
#chain(4633,1921,4)
#print pow (33*44,8,73)
#print pow((6*44*44),8,73)
#print 90411572%9509
#print chain(9509,9)
print show(evector(chain(12449,13)))
#print find(5)
#print euclidExt(8,9)
#print 792%73
#print (1281*233*116)%13561
print euclidExt((11341-351),12403)
print 11341-351
#print simpleform(9498)
#print 3279*93 % 8777
#print 8777/131
print 14400 - 14527
print 14500 - 14527
print 14456 - 14527
print 14508 - 14527
#print simpleform(82)
#print simpleform(71)
#print simpleform(27)
#print simpleform(39)
#print (pow(3,3)*13) % 12403
#print 12403/157
#print 72/3
#print pow(158,2,12403)

