products = [
    {"name": "Молоко", "price": "80", "stock": "10"},
    {"name": "Хлеб", "price": "50", "stock": "30"},
    {"name": "Сникерс", "price": "150", "stock": "20"}
]

products.append({"name": "Кола", "price": "100", "stock": "5"})

bad_snikers = {"name": "Сникерс", "price": "150", "stock": "20"}
products.remove(bad_snikers)

def show_all_products():
    total_money = 0
    print(f"--- В БАЗЕ СЕЙЧАС {len(products)} товаров ---. ")
    for product in products:
        print(f"Товар: {product['name']}, Цена: {product['price']}, Количество: {product['stock']}.")
        if int(product["stock"]) < 15:
            print(f"⚠️ ВНИМАНИЕ: {product['name']} заканчивается! осталось всего {(product['stock'])} штук. ")
        try:
            current_sum = int(product["price"]) * int(product["stock"])
            total_money += current_sum
        except:
            print("Ошибка: цена или количество должны быть числами!")
            continue
    print(total_money)

def add_new_product(name, price, stock):
    products.append({"name": name, "price": price, "stock": stock})

while True:
    new_name = input("Введите название: ")
    if new_name == "стоп":
        break
    new_price = input("Введите цену: ")
    new_stock = input("Введите количество: ")

    add_new_product(new_name, new_price, new_stock)
    show_all_products()