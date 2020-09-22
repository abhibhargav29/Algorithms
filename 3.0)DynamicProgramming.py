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
