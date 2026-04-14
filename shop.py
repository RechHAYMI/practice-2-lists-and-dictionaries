products = [
    {"name": "Молоко", "price": "80", "stock": "10"},
    {"name": "Хлеб", "price": "50", "stock": "30"},
    {"name": "Сникерс", "price": "150", "stock": "20"}
]

products.append({"name": "Кола", "price": "100", "stock": "5"})

bad_snikers = {"name": "Сникерс", "price": "150", "stock": "20"}
products.remove(bad_snikers)

total_money = 0

for product in products:
    print(f"Товар: {product['name']}, Цена: {product['price']}, Количество: {product['stock']}.")
    if int(product["stock"]) < 15:
        print(f"⚠️ ВНИМАНИЕ: {product['name']} заканчивается! осталось всего {(product['stock'])} штук. ")
    current_sum = int(product["price"]) * int(product["stock"])
    total_money += current_sum
print(total_money)    