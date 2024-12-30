def promotion_store(promotion, price):
    deduction = price * (promotion/100) 
    price = price - deduction
    return price

def price_item(price, kg):
    total = 0
    
    for i in range(int(kg)):
        total += price
    return total  