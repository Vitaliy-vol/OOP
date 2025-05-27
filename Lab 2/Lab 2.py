from abc import ABC, abstractmethod

# Принцип 1: Єдина відповідальність (SRP)
# Клас, який зберігає дані замовлення S
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id            # Ідентифікатор замовлення
        self.amount = amount                # Сума замовлення

# Принцип 2: Відкритість/закритість (OCP)
# Абстрактний базовий клас для платіжного методу O/C
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, order):
        pass  # Метод реалізується у підкласах

# Оплата карткою S
class CardPayment(PaymentMethod):
    def pay(self, order):
        print(f" Сплачено {order.amount} грн карткою. Замовлення №{order.order_id}")

# Оплата готівкою S
class CashPayment(PaymentMethod):
    def pay(self, order):
        print(f" Сплачено {order.amount} грн готівкою. Замовлення №{order.order_id}")

# Клас, який відповідає тільки за обробку платежу (SRP) S
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method  # Передаємо метод оплати

    def process(self, order: Order):
        self.payment_method.pay(order)  # Викликаємо оплату

# Головна функція
def main():
    # Створюємо замовлення
    order1 = Order(order_id=101, amount=350)

    # Обробка оплати карткою
    card_payment = CardPayment()
    processor1 = PaymentProcessor(card_payment)
    processor1.process(order1)

    # Обробка оплати готівкою
    cash_payment = CashPayment()
    processor2 = PaymentProcessor(cash_payment)
    processor2.process(order1)

# Запуск програми
if __name__ == "__main__":
    main()



#Single Responsibility Principle - Кожен клас повинен відповідати лише за одну логічну частину програми. Зміни в одній частині логіки не мають впливати на інші.
#Open/Closed Principle - Клас має бути відкритий для розширення, але закритий для зміни.Тобто ми можемо додавати нову поведінку, не змінюючи існуючий код.