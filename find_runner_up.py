if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
m=list(arr)
m.sort()
maximum=max(m)

old_i=0
for i in range(len(m)):
    if maximum > m[i] and m[i] != maximum:
        old_i=m[i]
        
print(old_i)