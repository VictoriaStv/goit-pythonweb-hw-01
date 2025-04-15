# goit-pythonweb-hw-01

## Завдання 1: Патерн Фабрика

- Реалізовано класи `Car` та `Motorcycle`, які успадковують абстрактний клас `Vehicle`.
- Створено фабрики для різних регіонів: `USVehicleFactory` та `EUVehicleFactory`.
- Запуск двигуна реалізовано через логування `INFO`.

## Завдання 2: SOLID

- Класи переписані згідно з принципами SOLID:
  - SRP — `Book` відповідає лише за дані книги.
  - OCP — `Library` розширювана без модифікацій.
  - LSP / ISP — через `LibraryInterface`.
  - DIP — `LibraryManager` працює з інтерфейсом.

## Команди для перевірки:

```bash
pipenv run python src/task1_factory.py
pipenv run python src/task2_solid.py
pipenv run mypy src/
pipenv run black src/
