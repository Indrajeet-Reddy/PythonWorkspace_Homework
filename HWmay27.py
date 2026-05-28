name = input("Enter consumer name : ")
ele_units = float(input("Enter units consumed by consumer : "))
ele_bill = 0
total_bill = 0
gst = 0



if 0 < ele_units <= 50:
    print("No bill")

elif 50 < ele_units <= 100:
    surcharge = 0
    price_per_unit = 5
    ele_bill = (ele_units * price_per_unit)+surcharge
    gst = ele_bill * 0.18
    total_bill =   ele_bill +  gst

elif ele_units > 100 :
    surcharge = 100 
    price_per_unit = 8
    ele_bill = (ele_units * price_per_unit)+surcharge 
    gst = ele_bill * 0.18
    total_bill = ele_bill + gst

elif ele_units >= 300 :
    surcharge = 500
    price_per_unit = 8
    ele_bill = (ele_units * price_per_unit )+surcharge
    gst = ele_bill * 0.18
    total_bill = ele_bill + gst

else:
    print("Wrong input")

if ele_bill>50:
    print("========================ELECTRICITY BILL SLIP============================")
    print(" ")
    print(f"Consumer Name = {name }")
    print("*"*50)
    print(f"Total unit consumed by consumer is = {ele_units }rs")
    print(f"Price for per unit is              = {price_per_unit }rs")
    print(f"Electricity bill                   = {ele_bill }rs")
    print(f"Surcharges is                      = {surcharge }rs")
    print(f"Gst                                = {gst }rs")
    print("-"*50)

    print(f"Total bill                         = {total_bill  }rs")
    print("-"*50)


