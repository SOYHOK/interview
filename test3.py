#num = 123456
num = int(input("Enter inter number: "))
test_num = 0
while (num>0):
    remainder = num % 10
    test_num = remainder + (test_num*10)
    num = num // 10
print("Reverse is : {}".format(test_num))

#2 mthod
#num = input("Enter a number: ")
#print('The reverse number is:')
#for i in reversed(num):
#   print(i, end='')