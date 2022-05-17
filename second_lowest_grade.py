if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        m=[]
        name = input()
        m.append(name)
        score = float(input())
        m.append(score)
        records.append(m)

# print()   
# print(records)
# print()

##loop the nested list and fetch the index[1] value from all the nexted list
mark=[]
for i in range(len(records)):
    mark.append(records[i][1])  
# print(mark)
# print()

#sort the list
mark.sort()
s_mark=mark
s_mark.reverse()
sorted_mark=s_mark
# print(sorted_mark)

##getting the minimum value from the list
minimum=min(sorted_mark)
# print(minimum)
# print()

#finding the second minimum from the list
old_i=0.0
for i in range(len(sorted_mark)):
    if minimum < sorted_mark[i] and sorted_mark[i] != minimum:
        old_i=sorted_mark[i]       
# print(old_i)
# print()

##get the name of the second maximum 
final_output=[]
for i in range(len(mark)):
    if records[i][1] == old_i:
        final_output.append(records[i][0])
    

# #sort and print the name

f=sorted(final_output)
for i in f:
    print(i)        

