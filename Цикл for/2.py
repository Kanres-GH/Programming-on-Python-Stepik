cnt = 0
sum = 0
a, b = int(input()), int(input())
for i in range(a, b+1):
    if i%3==0:
        cnt+=1
        sum += i
print(sum/cnt)