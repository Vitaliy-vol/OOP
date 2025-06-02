from abc import ABC, abstractmethod

# === Composite Pattern ===
# Абстрактний базовий клас, який представляє як окремі елементи меню, так і категорії (групи)
class MenuComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf (листок) у Composite — це конкретна позиція меню (наприклад, страва або напій)
class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self, indent=0):
        # Відображає назву страви з ціною з відступом
        print(' ' * indent + f'- {self.name}: {self.price:.2f} грн')

# Composite — категорія, яка може містити інші MenuComponent (інші категорії або страви)
class MenuCategory(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []  # список підпорядкованих компонентів

    def add(self, component):
        # Додає елемент (MenuItem або MenuCategory)
        self.items.append(component)

    def display(self, indent=0):
        # Відображає назву категорії та всі її елементи з відступом
        print(' ' * indent + f'Категорія: {self.name}')
        for item in self.items:
            item.display(indent + 2)

# === Facade Pattern ===
# Спрощує створення та заповнення меню. Приховує складну структуру Composite від користувача.
class RestaurantMenuFacade:
    def __init__(self):
        # Створюємо кореневу категорію меню (глобальний Composite)
        self.root_menu = MenuCategory("Головне меню")

    def add_category(self, category_name):
        # Створюємо підкатегорію та додаємо її до кореневого меню
        category = MenuCategory(category_name)
        self.root_menu.add(category)
        return category  # повертаємо, щоб додавати до неї страви

    def add_item_to_category(self, category, name, price):
        # Додаємо позицію до певної категорії
        item = MenuItem(name, price)
        category.add(item)

    def show_menu(self):
        # Виводимо всю структуру меню
        self.root_menu.display()

# === Клієнтський код ===
def main():
    menu = RestaurantMenuFacade()  # використовуємо фасад для роботи з меню

    # Додаємо категорії та страви через Facade
    drinks = menu.add_category("Напої")
    menu.add_item_to_category(drinks, "Капучино", 55.0)
    menu.add_item_to_category(drinks, "Чай зелений", 40.0)

    meals = menu.add_category("Гарячі страви")
    menu.add_item_to_category(meals, "Борщ український", 85.0)
    menu.add_item_to_category(meals, "Вареники з картоплею", 70.0)

    desserts = menu.add_category("Десерти")
    menu.add_item_to_category(desserts, "Наполеон", 60.0)
    menu.add_item_to_category(desserts, "Сирник", 50.0)

    print(" Меню ресторану:")
    menu.show_menu()

# Запуск програми
if __name__ == "__main__":
    main()
