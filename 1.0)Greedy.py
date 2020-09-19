class KnapsackItems():
    def __init__(self, ind,  val, weight):
        self.wt = weight
        self.val  = val
        self.index = ind
        self.net = val/weight

def ActivitySelection(arr):
    arr = sorted(arr, key=lambda x: x[1])
    Ans = []
    Ans.append(arr[0])
    for ele in arr:
        if(ele[0]>=Ans[-1][1]):
            Ans.append(ele)
        else:
            pass
    print("These tasks would be performed:", Ans)

def FractionaKnapsack(Items, n):
    Items = sorted(Items, key = lambda x: x.net, reverse=True)
    Ans = []
    wt = 0
    finVal = 0
    for item in Items:
        if(item.wt<=n-wt):
            Ans.append(item.index)
            finVal += item.val 
            wt+=item.wt 
        else:
            finVal += item.net*(n-wt)
            Ans.append(item.index)
            break 
    print("Selected items:", Ans)
    print("Total value:", finVal)

def JobSequencing(Jobs, time):
    Jobs = sorted(Jobs, key= lambda x: x[2], reverse=True)
    result = [False]*time
    ans = ["-"]*time
    profit = 0
    for job in Jobs:
        i = min(job[1]-1, time-1)
        while(i>=0):
            if(result[i]==False):
                result[i] = True
                ans[i] = job[0]
                profit += job[2]
                break
            i-=1
    print("Jobs:", ans)
    print("Profit:", profit)

#Activity selection
print()
arr= [[1,2],[5,7],[8,9],[5,9],[0,6],[3,4]]
ActivitySelection(arr)
print()

#Fractional Knapsack
I1 = KnapsackItems(1, 60, 10)
I2 = KnapsackItems(2, 40, 40)
I3 = KnapsackItems(3, 100, 20)
I4 = KnapsackItems(4, 120, 30)
cap = 50
items = [I1, I2, I3, I4]
FractionaKnapsack(items, cap)
print()

#Job Sequencing
Jobs = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
JobSequencing(Jobs, 3)
print()
