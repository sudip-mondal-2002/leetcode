ans=0
time=[30,20,150,100,40]
d=dict([[i,0]for i in range(60)])
for i in time:
    d[i%60]+=1
    s=(d[0]*(d[0]-1)+d[30]*(d[30]-1))//2
for i in range(1,30):
    s+=(d[i]*d[60-i])
print(s)
