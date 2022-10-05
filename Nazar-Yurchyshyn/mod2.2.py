from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
      Абстракція встановлює інтерфейс для «керуючої» частини двох ієрархій класів. 
      Вона містить посилання на об'єкт з ієрархії Реалізації та делегує йому всю справжню працю.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
      Можна розширити абстракцію без зміни класів реалізації.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
     Реалізація встановлює інтерфейс всім класів реалізації. Він не повинен відповідати інтерфейсу абстракції. 
     На практиці обидва інтерфейси можуть бути зовсім різними. Як правило, інтерфейс Реалізації надає лише примітивні операції, 
     тоді як Абстракція визначає операції вищого рівня, що ґрунтуються на цих примітивах.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Кожна Конкретна Реалізація відповідає певній платформі та реалізує інтерфейс Реалізації з використанням API цієї платформи.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    За винятком етапу ініціалізації, коли об'єкт абстракції пов'язується з певним об'єктом реалізації, клієнтський код повинен залежати тільки від
класу абстракції. Таким чином, клієнтський код може підтримувати будь-яку комбінацію абстракції та реалізації.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
 Клієнтський код повинен працювати з будь-якою попередньо налаштованою комбінацією абстракції та реалізації.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
