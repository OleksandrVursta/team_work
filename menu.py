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
    print("\n===== MENU =====")
    for dish in menu:
        print(
            f"{dish['name']} | "
            f"{dish['price']} грн | "
            f"{dish['description']}"
        )


def main():
    while True:
        print("\n1.Додати")
        print("2.Редагувати")
        print("3.Видалити")
        print("4.Порахувати")
        print("0.Вихід")

        choice = input("-> ")

        if choice == "1":
            pass

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

def edit_dish():
    name=input("Яку страву редагувати: ")

    for dish in menu:
        if dish["name"]==name:
            dish["price"]=float(input("Нова ціна: "))
            dish["description"]=input("Новий опис: ")
            dish["category"]=input("Нова категорія: ")
            print("Оновлено")
            return

    print("Страву не знайдено")

def show_by_category():
    category=input("Категорія: ")

    for dish in menu:
        if dish["category"]==category:
            print(dish["name"])

