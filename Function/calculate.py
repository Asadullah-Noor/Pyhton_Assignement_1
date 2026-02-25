def calculate_total(price,quantity):
    total=price*quantity
    return total
def discount_price(calculate_total,discount):
    discount_amount=(calculate_total*discount)/100
    final_price=calculate_total-discount_amount
    return final_price
print("Total Price :",calculate_total(10,5))
print("Discounted Price :",discount_price(calculate_total(10,5),5))
def temprature_conversion(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(temprature_conversion(25))