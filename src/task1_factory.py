from abc import ABC, abstractmethod
import logging
from typing import Protocol

# Логування
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# Абстрактний клас
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Конкретні класи
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


# Інтерфейс фабрики
class VehicleFactory(Protocol):
    def create_car(self, make: str, model: str) -> Vehicle: ...

    def create_motorcycle(self, make: str, model: str) -> Vehicle: ...


# Фабрика для США
class USVehicleFactory:
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


# Фабрика для ЄС
class EUVehicleFactory:
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


# Точка входу
def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
