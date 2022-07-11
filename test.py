#start = int(input("Enter the start number: "))
#end = int(input("Enter the end number: "))
#for num in range(start, end +1):
    #if num > 1:
        #for i in range (2, num):
        #    if (num%i) == 0:
         #       break
       # else:
          #  print("The prime number is: ",num)

count = 0
for num in range(10,100):
    if all(num%i!=0 for i in range (2,num)):
        print(num)
        count = count + 1
print("Count is: ",count)