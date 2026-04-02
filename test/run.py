def fetch_discount_rate():
    return 0.10

def get_discount(price: float):
    discount_rate = fetch_discount_rate()
    return price - (price * discount_rate)