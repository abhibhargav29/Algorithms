def LCS(X , Y): 
    m = len(X) 
    n = len(Y) 
   
    L = [[-1]*(n+1) for i in range(m+1)] 

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])   
    return L[m][n] 

def coinChange(coins, sum):
    C = [[-1]*(len(coins)+1) for j in range(sum+1)]
    for i in range(len(coins)+1):
        C[0][i] = 1
    for i in range(1, sum+1):
        C[i][0] = 0

    for i in range(1,sum+1):
        for j in range(1, len(coins)+1):
            C[i][j] = C[i][j-1]
            if(coins[j-1]<=i):
                C[i][j]+=C[i-coins[j-1]][j]
    return C[sum][len(coins)] 

def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)

    eD = [[-1]*(m+1) for i in range(n+1)]
    for i in range(0,m+1):
        eD[0][i] = i
    for i in range(0,n+1):
        eD[i][0] = i

    for i in range(1,n+1):
        for j in range(1,m+1):
            if(str1[j-1]==str2[i-1]):
                eD[i][j] = eD[i-1][j-1]
            else:
                eD[i][j] = 1+min(eD[i-1][j], eD[i][j-1], eD[i-1][j-1])
    return eD[n][m]

def LIS(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(0,n):
        j=i-1
        while(j>=0):
            if(arr[i]<=arr[j]):
                j-=1
            else:
                lis[i] = max(lis[i], 1+lis[j])
                j-=1
    return max(lis)

def BetterLIS(arr):
    n = len(arr)
    tail = [None]*n
    tail[0]=arr[0]
    length=1
    for ele in arr:
        if(ele>tail[length-1]):
            tail[length] = ele
            length+=1
        else:
            ind = BinarySearchTail(tail,-1,length-1,ele)
            tail[ind] = ele
    return length

def BinarySearchTail(arr, start, end, item):
    while(end-start>1):
        mid = start + (end-start)//2
        if(arr[mid]<=item):
            start = mid
        else:
            end = mid
    return end

def minCoins(arr, s):
    n = len(arr)
    mC = [float('inf')]*(s+1)
    mC[0] = 0

    for i in range(1, s+1):
        for j in range(n):
            if(i>=arr[j]):
                temp = mC[i-arr[j]]
                if(temp!=float('inf') and temp+1<mC[i]):
                    mC[i] = temp+1
    return mC[s]    

def minJumps(arr):
    n = len(arr)
    if(arr[0]==0):
        return float('inf')
    if(n==0 or n==1):
        return 0
    jumps = [float('inf')]*n
    jumps[0]=0
    for i in range(1, n):
        j=0
        while(j<i):
            if(j+arr[j]>=i):
                if(jumps[j]!=float('inf')):
                    jumps[i] = min(jumps[i], jumps[j]+1)
                    break
            j+=1
    return jumps[n-1]

def Knapsack(prices, weights, capacity):
    n = len(prices)
    dp = [[0]*(capacity+1) for i in range(n+1)]
    for i in range(0,capacity+1):
        dp[0][i] = 0
    for i in range(0,n+1):
        dp[i][0] = 0
    
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if(weights[i-1]<=j):
                dp[i][j] = max(dp[i-1][j], prices[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]

def cardGame(arr):
    n = len(arr)
    dpmat = [[0]*n for i in range(n)]
    for i in range(0,n-1):
        dpmat[i][i+1] = max(arr[i],arr[i+1])
    for gap in range(3,n):
        i=0
        while(i+gap<n):
            j=i+gap
            x = arr[i] + min(dpmat[i+2][j], dpmat[i+1][j-1])
            y = arr[j] + min(dpmat[i][j-2], dpmat[i+1][j-1])
            dpmat[i][j] = max(x, y)
            i+=1
    return dpmat[0][n-1]

def EggDropping(floors, eggs):
    trials = [[float('inf')]*eggs for i in range(floors+1)]
    for i in range(0, eggs):
        trials[0][i] = 0
        trials[1][i] = 1
    for i in range(2, floors+1):
        trials[i][0] = i
    for i in range(2, floors+1):
        for j in range(1,eggs):
            for x in range(1,i+1):
                T = 1+max(trials[x-1][j-1], trials[i-x][j])
                trials[i][j] = min(trials[i][j], T)
    return trials[floors][eggs-1]

def countBST(n):
    if(n==0):
        return 0
    ans = [0]*(n+1)
    ans[0] = 1
    for i in range(1,n+1):
        res=0
        for j in range(0,i):
            res+=ans[j]*ans[i-j-1]
        ans[i] = res
    return ans[n]

#Longest common subsequence
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", LCS(X, Y))

#Coins Change
coins = [1, 2, 3]  
sum = 4
print("Number of ways:",coinChange(coins, sum))

#Edit Distance
str1 = "sunday"
str2 = "saturday"
print("Operations:",editDistance(str1, str2))

#Longest Increasing Subsequence
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Length of LIS:", LIS(arr))

#Minimum coins change
Coins = [9, 6, 5, 1]  
V = 11
print("Number of coins:",minCoins(Coins, V))

#Minimum jumps to reach end
arr = [1, 3, 6, 1, 0, 9] 
print('Minimum Jumps:', minJumps(arr))

#0/1 Knapsack Problem
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50 
print("Value in Knapsack:",Knapsack(val, wt, W))

#Optimal Strategy for game 
arr3 = [ 20, 30, 2, 2, 2, 10] 
print("Maximum sum in card game:", cardGame(arr3))

#Eggs Dropping
floors = 36
eggs = 2
print("Number of egg dropping trials:",EggDropping(floors, eggs))

#Count BST
n = 5
print("Number of BST possible:",countBST(n))
