# WAF to converrt USD to INR 

def convert():
    usd = int(input("Enter total usd you have : "))
    rate = float(input("Enter convert rate : "))
    
    print(usd,"$ = ₹",usd*rate)

convert()