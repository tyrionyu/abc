sum=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    sum+=i
    i+=1
print('1~100之间的偶数和：',sum) 