# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, data):
#         new_node = Node(data)
#         #insert into empty tree
#         if self.root is None:
#             self.root = new_node
#             return
#
#         current = self.root
#
#         while True:
#             if data < current.data:
#                 if current.left is None:
#                     current.left = new_node
#                     return
#                 current = current.left
#             elif data > current.data:
#                 if current.right is None:
#                     current.right = new_node
#                     return
#                 current = current.right
#             else:
#                 print("Data is already present")
#                 break
#
# tree = BinarySearchTree()


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class ProductTree:
    def __init__(self):
        self.root = None

    def add_product(self, product):
        new_node = Node(product)
        if self.root is None:
            self.root = new_node
            return True
        current = self.root
        while True:
            if product.id < current.product.id:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif product.id > current.product.id:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else:
                return False

    def find_product(self, product_id):
        current = self.root
        while current:
            if product_id == current.product.id:
                return current.product
            elif product_id < current.product.id:
                current = current.left
            else:
                current = current.right
        return None

    def contains(self, product_id):
        return self.find_product(product_id) is not None

    def show_products(self):
        def _in_order(node):
            if node:
                _in_order(node.left)
                print(f"{node.product.id} — {node.product.name} — {node.product.price} грн")
                _in_order(node.right)

        _in_order(self.root)

    def get_cheapest(self):
        if self.root is None:
            return None
        cheapest = self.root.product

        def _search(node):
            nonlocal cheapest
            if node:
                if node.product.price < cheapest.price:
                    cheapest = node.product
                _search(node.left)
                _search(node.right)

        _search(self.root)
        return cheapest

    def get_most_expensive(self):
        if self.root is None:
            return None
        expensive = self.root.product

        def _search(node):
            nonlocal expensive
            if node:
                if node.product.price > expensive.price:
                    expensive = node.product
                _search(node.left)
                _search(node.right)

        _search(self.root)
        return expensive

    def count_products(self):
        def _count(node):
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)


def main():
    tree = ProductTree()

    initial_products = [
        Product(50, "Laptop", 30000),
        Product(25, "Mouse", 800),
        Product(75, "Monitor", 12000),
        Product(10, "Cable", 250),
        Product(35, "Keyboard", 1500),
        Product(60, "Headphones", 2000)
    ]
    for p in initial_products:
        tree.add_product(p)

    while True:
        print("\n--- Меню каталогу ---")
        print("1. Показати всі товари")
        print("2. Додати новий товар")
        print("3. Знайти товар за ID")
        print("4. Перевірити наявність за ID")
        print("5. Знайти найдешевший товар")
        print("6. Знайти найдорожчий товар")
        print("7. Показати загальну кількість товарів")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        if choice == "1":
            print("\nКаталог товарів:")
            if tree.root is None:
                print("Каталог порожній")
            else:
                tree.show_products()

        elif choice == "2":
            try:
                p_id = int(input("Введіть ID товару: "))
                name = input("Введіть назву товару: ")
                price = float(input("Введіть ціну товару: "))
                new_prod = Product(p_id, name, price)
                if tree.add_product(new_prod):
                    print("Товар успішно додано!")
                else:
                    print("Помилка: Товар з таким ID вже існує!")
            except ValueError:
                print("Некоректне введення даних.")

        elif choice == "3":
            try:
                p_id = int(input("Введіть ID товару: "))
                prod = tree.find_product(p_id)
                if prod:
                    print(f"Товар знайдено: {prod.name}\nЦіна: {prod.price} грн")
                else:
                    print("Товар не знайдено")
            except ValueError:
                print("Некоректний ID.")

        elif choice == "4":
            try:
                p_id = int(input("Введіть ID для перевірки: "))
                if tree.contains(p_id):
                    print(f"Товар з ID {p_id} існує в каталозі.")
                else:
                    print(f"Товар з ID {p_id} відсутній.")
            except ValueError:
                print("Некоректний ID.")

        elif choice == "5":
            prod = tree.get_cheapest()
            if prod:
                print(f"Найдешевший товар: {prod.name} ({prod.price} грн)")
            else:
                print("Каталог порожній")

        elif choice == "6":
            prod = tree.get_most_expensive()
            if prod:
                print(f"Найдорожчий товар: {prod.name} ({prod.price} грн)")
            else:
                print("Каталог порожній")

        elif choice == "7":
            print(f"Загальна кількість товарів у дереві: {tree.count_products()}")

        elif choice == "0":
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()


