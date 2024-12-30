def promotion_store(promotion, price):
    deduction = price * (promotion/100) 
    price = price - deduction
    return price