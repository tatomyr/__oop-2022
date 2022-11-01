from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """Інтерфейс Builder визначає методи для створення різних частин об'єктів продукт."""
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    @abstractmethod
    def produce_part_a(self) -> None:
        pass
    @abstractmethod
    def produce_part_b(self) -> None:
        pass
    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    """Класи Concrete Builder слідують інтерфейсу Builder і надають конкретні реалізації етапів побудови. Ваша програма може мати
кілька варіацій конструкторів, реалізованих по-різному."""
    def __init__(self) -> None:
        """
       Новий екземпляр builder повинен містити порожній об'єкт product, який використовується в подальшій збірці.
        """
        self.reset()
    def reset(self) -> None:
        self._product = Product1()
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    def produce_part_a(self) -> None:
        self._product.add("PartA1")
    def produce_part_b(self) -> None:
        self._product.add("PartB1")
    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product1():
    def __init__(self) -> None:
        self.parts = []
    def add(self, part: Any) -> None:
        self.parts.append(part)
    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")
class Director:
    """
    Директор несе відповідальність тільки за виконання етапів будівництва в
    певної послідовності. Це корисно при виробництві виробів відповідно до
певним замовленням або конфігурацією. Строго кажучи, клас Director є
необов'язковим, оскільки клієнт може безпосередньо керувати конструкторами.
    """
    def __init__(self) -> None:
        self._builder = None
    @property
    def builder(self) -> Builder:
        return self._builder
    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        Директор працює з будь-яким екземпляром builder, який передається клієнтським кодом
        до нього. Таким чином, клієнтський код може змінити остаточний тип новоствореного
        зібраний продукт.
        """
        self._builder = builder
    """
    Директор може створити кілька варіантів продукту, використовуючи один і той же
    Будівельні сходи.
    """
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()
    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
if __name__ == "__main__":
    """
    Клієнтський код створює об'єкт builder, передає його директору, а потім
ініціює процес побудови. Кінцевий результат витягується з об'єкта
builder.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder
    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()
    print("\n")
    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()
    print("\n")
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
