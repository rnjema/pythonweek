"""
Cost price (in Rs)				        Tax
			>100,000					15%
			>50,000 and <=100,000		10%
			<=50,000                    %5
"""
def taxCalc(price):
    tax = 0
    msgFormat = "The tax levied on a bike that costs  R{} is {}%"
    if price > 100000:
        tax = 15
        print(msgFormat.format(price, tax))
    elif(50000 < price <= 100000):
        tax = 10
        print(msgFormat.format(price,tax))
    elif(0 < price <= 50000):
        tax = 5
        print(msgFormat.format(price,tax))
    else:
        print("Invalid PRICE!!!")

try:
    bikePrice = int(input("Please enter price of bike: "))
except Exception as e:
    print("An ERROR occurred : ", e)
else:
    taxCalc(bikePrice)

