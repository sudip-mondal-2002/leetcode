def main(nums):
    n=len(nums)
    dp=[ [0 for i in range(n)] for j in range(n)]
    for length in range(n):
        for i in range(n-length):
            j=i+length
            dp[i][j]=assignvalue(i,j,dp,nums,n)
    return (dp[0][n-1])
def assignvalue(i,j,dpl,l,n):
    templist=[]
    for k in range(i,j+1):
        left=0
        right=0
        if k!=i:
            left=dpl[i][k-1]
        if k!=j:
            right=dpl[k+1][j]
        leftp=1
        rightp=1
        if i!=0:
            leftp=l[i-1]
        if j!=n-1:
            rightp=l[j+1]
        middle=leftp*rightp*l[k]
        templist.append(left+right+middle)
    return (max(templist))
            
print(main([3,1,5,8]))
