#List =[2,1,3,5,4,6,8,9,7]
#for i in range(len(List)):
 #   for j in range(i+1,len(List)):
  #      if List[i] > List[j]:
   #         List[i],List[j]=List[j],List[i]
#print(List)

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)