class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id должен быть типа int")
        if not isinstance(name, str):
            raise TypeError("name должен быть типа str")
        if not isinstance(pages, int):
            raise TypeError("pages должен быть типа int")
        if pages > 0:
            self.id_ = id_
            self.name = name
            self.pages = pages
        else:
            raise ValueError("Число страниц в книге должно быть больше нуля!")
    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'
class Library:
    def __init__(self, books=[]):
        self.books = books
    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[len(self.books) - 1].id_ + 1
    def get_index_by_book_id(self, check_):
        index_ = None
        for i, val in enumerate(self.books):
            if val.id_ == check_:
                index_ = i
        if index_ == None:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return index_


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]





# TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
