n = int(input())
for _ in range(n):
    k = list(map(int,input().split()))
    k.sort()
    if len(k)%2 == 0:
        evee = len(k)//2
        print(k[evee-1])
    elif len(k)%3 == 0:
        j = (len(k)+1)//2
        print(k[j-1])
