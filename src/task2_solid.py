from abc import ABC, abstractmethod
import logging
from typing import List

# Логування
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# Клас Book
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Інтерфейс
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# бібліотека
class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, title: str) -> None:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                logger.info(f"Книга '{title}' видалена з бібліотеки.")
                return
        logger.info(f"Книгу '{title}' не знайдено в бібліотеці.")

    def get_books(self) -> List[Book]:
        return self._books


# Клас керування бібліотекою
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            book = Book(title, author, int(year))
            self.library.add_book(book)
        except ValueError:
            logger.info("Невірний формат року. Будь ласка, введіть число.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("У бібліотеці немає жодної книги.")
        for book in books:
            logger.info(str(book))


#
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Вихід з програми.")
                break
            case _:
                logger.info("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
