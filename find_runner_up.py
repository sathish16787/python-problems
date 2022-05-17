if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
# m=list(arr)
# m.sort()
# l=m

l=list(arr)
maximum=max(l)

old_i=0
for i in range(len(l)):
    if maximum > l[i] and l[i] != maximum:
        old_i=l[i]
        
print(old_i)