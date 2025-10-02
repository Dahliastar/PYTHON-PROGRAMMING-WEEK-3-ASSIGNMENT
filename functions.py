price = float(input("Enter the price:")) 
discount_percent = float(input("Enter the discount percentage:")) 

def calculate_discount(price, discount_percent): 
    if discount_percent >= 20:
         discount = price * (discount_percent / 100) 
         final_price = price - discount
         return final_price
    else: 
        print(price)

calculate_discount(price, discount_percent)
