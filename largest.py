a,b,c=map(int,input("enter three numbers: ").split())
ch=int(input("enter 1 for max & 0 for min:"))
if(ch==1):
    if(a>b and a>c):
        print(f"{a} is maximum")
    elif(b>a and b>c):
        print(f"{b} is maximum")
    else:
        print(f"{c} is maximum")
else:
    if(a<b and a<c):
        print(f"{a} is minimum")
    elif(b<a and b<c):
        print(f"{b} is minimum")
    else:
        print(f"{c} is minimum")


