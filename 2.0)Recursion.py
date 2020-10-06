#values has a,b and c
def rodCutting(rod, values):
    a,b,c = values
    #base cases
    if(rod==0):
        return 0
    elif(rod<0):
        return -1
    cnt = 0
    #recursion
    cnt= max(cnt, 1 + rodCutting(rod-a, values))
    cnt= max(cnt, 1 + rodCutting(rod-b, values))
    cnt= max(cnt, 1 + rodCutting(rod-c, values))
    #ans
    if(cnt==0):
        return -1
    else:
        return cnt

def towerOfHanoi(n, startRod="A",auxRod="B",endRod="C"):
    #base case
    if(n==1):
        print("Move rod 1 from {} to {}".format(startRod, endRod))
        return
    #recursion from a to b
    towerOfHanoi(n-1, startRod, endRod, auxRod)
    print("Move rod {} from {} to {}".format(n, startRod, endRod))
    #recusrion from b to c
    towerOfHanoi(n-1, auxRod, startRod, endRod)

def josephusProblem(n,k):
    #base case
    if(n==1):
        return 0
    #recursion plus balancing index
    return (josephusProblem(n-1, k) + k) % n  
