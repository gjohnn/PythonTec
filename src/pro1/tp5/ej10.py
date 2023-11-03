from functions import discount

cart_to_buy = {"producto1": 100, "producto2": 50, "producto3": 75}

discount_per_product = {"producto1": 10, "producto3": 5}

price_final = discount(cart_to_buy, discount_per_product)
print(f"El precio final de la compra es: ${price_final}")
