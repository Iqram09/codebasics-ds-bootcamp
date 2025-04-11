from fastapi import FastAPI

app = FastAPI()

food_items ={
    "indian": ["Samosa","Dosa"],
    "american":["Apple pie", "Chicken sandwich"],
    "italian": ["Pizza", "Ravioli"]
}

@app.get("/")
def read_root():
    return {"Hello": "d"}

@app.get("/name/{name}")
def read_item(name: str):
    return {"name": name}

@app.get("/items/{items_id}")
def read_item(items_id: str, q: str = None):
    return {"items": food_items.get(items_id, "Category not found"), "q": q}

coupons = {
    "WELCOME10": 10,  # 10% discount
    "SALE20": 20,  # 20% discount
    "VIP30": 30  # 30% discount
}

@app.get("/apply-coupon/{coupon_code}")   # /apply-coupon/YOURCODEHERE?price=100
def apply_coupon(coupon_code: str, price: float):
    if coupon_code in coupons:
        discount = (coupons[coupon_code] / 100) * price
        final_price = price - discount
        return {
            "Original Price": price,
            "Discount": f"{coupons[coupon_code]}%",
            "Final Price": final_price
        }
    else:
        return {"error": "Invalid coupon code"}
