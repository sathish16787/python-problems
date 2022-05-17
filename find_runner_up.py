if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

list_value=list(arr)
maximum_from_list_value=max(list_value)

old_i=0
for i in range(len(list_value)):
    if list_value[i] < maximum_from_list_value and list_value[i] != maximum_from_list_value:
        old_i=list_value[i]
        
print(old_i)