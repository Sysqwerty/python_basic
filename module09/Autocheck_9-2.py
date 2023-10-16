DEFAULT_DISCOUNT = 0.05
customer = {"name": "Boris", "discount": 0.15}
customer2 = {"name": "Dima"}
customer3 = {'name': 'Olga', 'discount': 0}


def get_discount_price_customer(price: float, customer: dict):
    customer_discount = customer.get("discount")
    discount = customer_discount if "discount" in customer.keys() else DEFAULT_DISCOUNT
    price = price * (1 - discount)
    return price


print(get_discount_price_customer(100, customer))
print(get_discount_price_customer(100, customer2))
print(get_discount_price_customer(100, customer3))
