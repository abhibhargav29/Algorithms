def rodCutting(rod, values):
    a,b,c = values
    if(rod==0):
        return 0
    elif(rod<0):
        return -1
    cnt = 0
    cnt= max(cnt, 1 + rodCutting(rod-a, values))
    cnt= max(cnt, 1 + rodCutting(rod-b, values))
    cnt= max(cnt, 1 + rodCutting(rod-c, values))
    if(cnt==0):
        return -1
    else:
        return cnt

def towerOfHanoi(n, startRod="A",auxRod="B",endRod="C"):
    if(n==1):
        print("Move rod 1 from {} to {}".format(startRod, endRod))
        return
    towerOfHanoi(n-1, startRod, endRod, auxRod)
    print("Move rod {} from {} to {}".format(n, startRod, endRod))
    towerOfHanoi(n-1, auxRod, startRod, endRod)

def josephusProblem(n,k):
    if(n==1):
        return 0
    return (josephusProblem(n-1, k) + k) % n  