import math
def distance(a,b):
    if len(a)!=(len(b)):
        print "a and b are not equal size"
    total=0
    for i in xrange(len(a)):
        total+=(a[i][0]-b[i][0])**2+(a[i][1]-b[i][1])**2
    return math.sqrt(total)
print distance([(1,1),(2,2)],[(0,0),(0,0)])
