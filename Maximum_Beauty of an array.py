def popcount(x):
    return bin(x).count('1')

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[:n]

    beauty = sum(popcount(x) for x in a)   #current beauty

    while k > 0:
        index = -1
        for i in range(n):
            before = popcount(a[i])
            after = popcount(a[i] + 1)
            if after > before:
                index = i
                break
        
        if index == -1:
            break
        
        a[index] += 1
        beauty += 1
        k -= 1

    print(beauty)
