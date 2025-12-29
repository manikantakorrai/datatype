num = int(input("enter a number:"))
count =0
flag =0
for i in range(1,num + 1):
    if i%2 ==0:
        count +=1
    else:
        flag +=1
print(f"{count}even numbers between 1 and{num}")
print(f"{count}odd numbers between 1 and{num}")
