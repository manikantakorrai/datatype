p = float(input("enter the principle:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time:"))
amount=p*(1+r/100)*r*t
print("amount:",amount)
ci=amount-p
print("compound interest:",ci)
