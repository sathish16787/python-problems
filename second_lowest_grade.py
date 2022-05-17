if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        m=[]
        name = input()
        m.append(name)
        score = float(input())
        m.append(score)
        records.append(m)


##loop the nested list and fetch the index[1] value from all the nexted list
mark=[]
for i in range(len(records)):
    mark.append(records[i][1])  


#sort the list
mark.sort()
mark.reverse()


##getting the minimum value from the list
minimum=min(mark)


#finding the second minimum from the list
old_i=0.0
for i in range(len(mark)):
    if minimum < mark[i] and mark[i] != minimum:
        old_i=mark[i]       


##get the name of the second maximum 
final_output=[]
for i in range(len(mark)):
    if records[i][1] == old_i:
        final_output.append(records[i][0])
    

# #sort and print the name

f=sorted(final_output)
for i in f:
    print(i)        

