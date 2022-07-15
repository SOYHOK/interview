# program to check weather
num = int(input("Enter number: "))
Temp = num;
reverse_Temp = 0
while (num>0):
    w = num % 10
    reverse_Temp = w + (reverse_Temp*10)
    num = num // 10
print("Reverse is: ", reverse_Temp)
if (reverse_Temp==num):
    print("True")
else: 
    print("Fale")
