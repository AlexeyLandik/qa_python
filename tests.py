import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2  # закомментировал этот прекод, тк он был не рабочий
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест №1. Фильмы с длиной названия больше допустимой (40 символов) не добавляются в коллекцию
    def test_add_new_book_length_name_more40(self):
        collector = BooksCollector()

        collector.add_new_book('В этом названии книги 41символ.Тест длины')

        assert len(collector.books_genre) == 0

    # Тест №2. Одну и ту же книгу можно добавить только один раз
    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.books_genre) == 1

    # Тест №3. Жанр устанавливается только если книга есть в словаре и жанр в списке жанров
    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Колобок', 'Комедии'],
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
            ['English', 'Ужасы'],
        ]
    )
    def test_set_book_genre_name_in_books_genre_and_genre_in_genre_dict(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    # Тест №4. Получить жанр книги по имени. Имя и жанр есть в словаре books_genre
    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Колобок', 'Комедии'],
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
        ]
    )
    def test_get_book_genre_get_genre_by_name(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    # Тест №5. Получить список по жанру. Добавить две книги с разными валидными жанрами. Получить список по жанру
    def test_get_books_with_specific_genre_two_books_with_different_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Что делать, если ваш кот хочет вас убить']

    # Тест №6. Получить текущий словарь. Добавить две книги и жанр. Получить актуальный словарь
    def test_get_books_genre_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')

        assert collector.get_books_genre() == {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Детективы'
        }

    # Тест №7. Получить список книг для детей. Добавить две книги с возрастным рейтингом и без него
    def test_get_books_for_children_two_books_with_different_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')

        assert collector.get_books_for_children() == ['Колобок']

    # Тест №8. Добавить книгу в избранное.
    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 2

    # Тест №9. Добавить две книги в избранное и удалить одну. ОР: Длина списка избранных == 1
    def test_delete_book_from_favorites_delete_one_of_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 1

    # Тест №10. Добавить в избранное две книги. Получить актуальный список
    def test_get_list_of_favorites_books_list_of_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]
