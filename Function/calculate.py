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


# Grade Calculator
def grade_calculator(*marks):
    total_marks=sum(marks)
    average_marks=total_marks/len(marks)
    print("Total Marks :",total_marks)
    print("Average Marks :",average_marks)
    if total_marks>=90:
        return "A"
    elif total_marks>=80:
        return "B"
    elif total_marks>=70:
        return "C"
    elif total_marks>=60:
        return "D"
    else:
        return "F"
print("Grade :",grade_calculator(85,23,4,5,2,5,25,5,2,5,25,5,2,5,25,5,2,5,25,5,2,5,25))