import sys
sys.setrecursionlimit(10**6)

def graduateWays(N, missLeft, totalAllowed):
    global dp
    waysWithMiss, waysWithoutMiss = 0, 0

    if N==0:
        if missLeft < 0:
            return 0
        return 1
    
    if dp[N][missLeft] != -1:
        return dp[N][missLeft]

    if missLeft > 0:
        waysWithMiss =  graduateWays(N-1, missLeft-1, totalAllowed)

    waysWithoutMiss = graduateWays(N-1, totalAllowed, totalAllowed)

    ans = waysWithMiss + waysWithoutMiss

    dp[N][missLeft] = ans

    return ans

missAllowed = 3
noOfDays = int(input("Enter the no. of Days "))

dp = []
for i in range(noOfDays+1):
    dp.append([-1]*(missAllowed+1))

ans = graduateWays(noOfDays, missAllowed, missAllowed)

# for i in range(len(dp)):
#     print(dp[i])
#     print("\n")

if dp[noOfDays-1][missAllowed-1] == -1:
    print("{}/{}".format(1,ans))
else:
    print("{}/{}".format(dp[noOfDays-1][missAllowed-1],ans))