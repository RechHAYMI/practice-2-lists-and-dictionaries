item = {
    "name": "butterfly",
    "price": 67,
    "rare": "Arcana"
}

inventory = [item]

total_value = 0
for item in inventory:
    total_value += item ["price"]
print(f"Итого: {total_value}")