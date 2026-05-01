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

def total_price():
    total=sum(d["price"] for d in menu)
    print(total)

def category_price():
    cat=input("Категорія: ")

    total=sum(
        d["price"]
        for d in menu
        if d["category"]==cat
    )

    print(total)

def sort_price_asc():
    menu.sort(key=lambda x:x["price"])


def sort_price_desc():
    menu.sort(key=lambda x:x["price"],reverse=True)
def delete_by_name():
    name=input("Назва: ")

    global menu
    menu=[dish for dish in menu if dish["name"]!=name]

    print("Видалено")
def delete_by_category():
    category=input("Категорія: ")

    global menu
    menu=[dish for dish in menu if dish["category"]!=category]

def count_dishes():
    print("Кількість:",len(menu))

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

