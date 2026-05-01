menu = [
    {
        "name": "Борщ",
        "price": 120,
        "description": "Український борщ"
    },
    {
        "name": "Піца",
        "price": 200,
        "description": "4 сири"
    }
]


def show_menu():
    print("\n==============================")

    for dish in menu:
        print(f"Назва: {dish['name']}")
        print(f"Категорія: {dish['category']}")
        print(f"Ціна: {dish['price']} грн")
        print(f"Опис: {dish['description']}")
        print("-------------------------")


def main():
    while True:
        print("\n1.Додати")
        print("2.Редагувати")
        print("3.Видалити")
        print("4.Порахувати")
        print("0.Вихід")

        choice = input("-> ")

        if choice=="1":
            add_dish()

        elif choice == "2":
            pass

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "0":
            break

        show_menu()


main()

def add_dish():
    name = input("Назва: ")
    category = input("Категорія: ")
    description = input("Опис: ")

    price = float(input("Ціна: "))

    if price < 0:
        print("Ціна не може бути від'ємною")
        return

    menu.append({
        "name": name,
        "category": category,
        "price": price,
        "description": description
    })

    print("Додано")