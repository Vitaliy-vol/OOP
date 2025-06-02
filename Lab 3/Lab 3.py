import copy  # Імпортуємо модуль для глибокого копіювання об'єктів

# Клас-прототип (Prototype)
class Document:
    def __init__(self, title, author, content):
        # Конструктор для створення нового документа
        self.title = title
        self.author = author
        self.content = content

    def clone(self):
        # Метод клонування — суть патерна Prototype
        # Створює глибоку копію поточного об'єкта (усі властивості копіюються)
        return copy.deepcopy(self)

    def display(self):
        # Метод для виводу вмісту документа
        print(f"Заголовок: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Вміст: {self.content}")
        print("-" * 30)


# Головна функція — демонстрація патерна Prototype
def main():
    # Створюємо оригінальний документ (оригінальний об'єкт-прототип)
    original = Document("Протокол", "Іваненко І.І.", "Це початковий текст документа.")
    print("Оригінал:")
    original.display()

    # Створюємо перший клон з оригіналу (використовується метод clone())
    clone1 = original.clone()  # ← Патерн Prototype у дії
    # Вносимо зміни у копію, не змінюючи оригінал
    clone1.title = "Копія протоколу"
    clone1.author = "Петренко П.П."
    clone1.content = "Це змінена копія документа."

    print("Клон 1:")
    clone1.display()

    # Створюємо ще один клон з того ж оригіналу
    clone2 = original.clone()  # ← Ще один приклад використання патерна Prototype
    # Змінюємо інші властивості
    clone2.title = "Чернетка"
    clone2.content = "Чернетка майбутнього документа."

    print("Клон 2:")
    clone2.display()


# Точка входу у програму
if __name__ == "__main__":
    main()
