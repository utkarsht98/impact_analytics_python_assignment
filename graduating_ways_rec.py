import sys
sys.setrecursionlimit(10**6)

def graduateWays(N, missLeft, totalAllowed):
    global missGraduationCount
    waysWithMiss, waysWithoutMiss = 0, 0

    if N==0:
        if missLeft < 0:
            return 0
        return 1
    
    if N==1:
        if missLeft >= 1:
            missGraduationCount += 1

    if missLeft > 0:
        waysWithMiss =  graduateWays(N-1, missLeft-1, totalAllowed)

    waysWithoutMiss = graduateWays(N-1, totalAllowed, totalAllowed)

    ans = waysWithMiss + waysWithoutMiss

    return ans

missGraduationCount = 0
consecutiveAbsentAllowed = 3
noOfDays = 10

ans = graduateWays(noOfDays, 3, 3)
print("{}/{}".format(missGraduationCount,ans))
