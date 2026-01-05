#compute edit distance by iteration using the Levenshtein cost.
#author: vidya rangantahan

import string

def editDistance(str1, str2, m, n):
    dp =  [[0 for x in range(m + 1)] for y in range(n + 1)] 

    for i in range(m+1):
        for j in range(n+1):
            if (i==0):
                dp[i][j] = j
            elif(j==0):
                dp[i][j] = i
            elif(str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                cost = 0 if(str1[i-1] == str2[j-1]) else 2
                dp[i][j] = min(dp[i][j-1] + 1, #insert
                               dp[i-1][j] + 1 , #delete
                               dp[i-1][j-1] + cost #substitution
                              )
                
    return dp[m][n]

str1="sunday"
str2="monday"

rc = editDistance(str1, str2, len(str1), len(str2))
print("edit distance of strings are: \n", rc);
