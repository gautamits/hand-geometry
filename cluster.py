#clusters one dimensional array
def cluster(xaxis):
    #print xaxis
    result=[]
    temp=[]
    temp.append(xaxis[0])
    d=30
    for i in xrange(1,len(xaxis)):
        if xaxis[i]-xaxis[i-1] < d:
            temp.append(xaxis[i])
        else:
            result.append(temp)
            temp=[]
            temp.append(xaxis[i])
    result.append(temp)
    return result
def unique(arr):
    arr=sorted(arr)
    #print arr
    xaxis=[i for (i,j) in arr]
    result=cluster(xaxis)
    #print result
    mapx = {}
    for (i,j) in arr:
        mapx[i] = j
    mapy={}
    for (i,j) in arr:
        mapy[j]=i
    for i in xrange(0,len(result)):
        for j in xrange(0,len(result[i])):
            result[i][j]=mapx[result[i][j]]
    minimum=[]
    for i in result:
        minimum.append(min(i))
    #print minimum
    ret=[]
    for i in minimum:
        ret.append((mapy[i],i))
    return ret


print unique([(240, 549), (404, 150), (410, 139), (427, 129), (611, 59), (633, 59), (742, 67), (765, 76), (905, 154), (921, 168), (924, 237), (926, 182)])
