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
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест добавляет книги с разной длиной названия. Будет добавлена только книга с корректной длиной названия.
    def test_add_new_book_add_book_with_different_names_lengths_should_add_only_correct_name_length(self):
        collector = BooksCollector()
        collector.add_new_book('Игры, в которые играют люди. Психология человеческих взаимоотношений')
        collector.add_new_book('Пять травм, которые мешают быть самим собой')
        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 1

        if 'Мечтают ли андроиды об электроовцах?' in collector.get_books_genre():
            book_in_genre = True
        else:
            book_in_genre = False
        assert book_in_genre == True

    # Тест добавляет 2 раза книгу с одним и тем же названием. Книга будет добавлена только один раз.
    def test_add_new_book_add_book_with_the_same_name(self):
        collector = BooksCollector()
        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        assert len(collector.get_books_genre()) == 1

    #Тест добавляет книгу и устанавливает ей жанр 'Фантастика'. Будет добавлена 1 книга с жанром 'Фантастика'.
    def test_set_book_genre_set_genre_scifi(self):
        collector = BooksCollector()
        collector.add_new_book('Пробуждение Левиафана')
        collector.set_book_genre('Пробуждение Левиафана', 'Фантастика')
        assert collector.get_book_genre('Пробуждение Левиафана') == 'Фантастика'

    #Тест добавляет книгу и устанавливает ей несуществующий в списке жанр. Жанр у добавленной книги не изменится.
    def test_set_book_genre_set_not_exist_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пробуждение Левиафана')
        collector.set_book_genre('Пробуждение Левиафана', 'Драма')
        assert collector.get_book_genre('Пробуждение Левиафана') == ''

    #Тест добавляет книгу и устанавливает ей жанр 'Фантастика'. Меняет жанр на "Ужасы". Жанр изменится.
    def test_set_book_genre_change_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пробуждение Левиафана')
        collector.set_book_genre('Пробуждение Левиафана', 'Фантастика')
        collector.set_book_genre('Пробуждение Левиафана', 'Ужасы')
        assert collector.get_book_genre('Пробуждение Левиафана') == 'Ужасы'

    #Тест добавляет книгу и устанавливает жанр для несуществующей книги. Для добавленной книги жанр не применяется.
    def test_set_book_genre_set_not_exist_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пробуждение Левиафана')
        collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')
        assert collector.get_book_genre('Пробуждение Левиафана') == ''

    #Тест проверяет количество книг по каждому жанру. Количество должно соответствовать ожидаемому.
    @pytest.mark.parametrize(
        'genre, expected_count',[
            ['Фантастика', 4],
            ['Ужасы', 3],
            ['Детективы', 2],
            ['Мультфильмы', 2],
            ['Комедии', 2],
        ])
    def test_get_books_with_specific_genre_get_all_genres(self, book_shelf, genre, expected_count):
        assert len(book_shelf.get_books_with_specific_genre(genre)) == expected_count


    #Тест проверяет количество книг, подходящих для детей. Должно соответствовать 8.
    def test_get_books_for_children_two_book_for_adult_two_book_for_children(self, book_shelf):
        assert len(book_shelf.get_books_for_children()) == 8

    #Тест добавляет книги в Избранное. 2 раза добавляет одну и ту же книгу, книга должна добавиться один раз.
    def test_add_book_in_favorites_add_two_book_in_favorites(self, book_shelf):
        book_shelf.add_book_in_favorites('Пробуждение Левиафана')
        book_shelf.add_book_in_favorites('Хребты безумия')
        book_shelf.add_book_in_favorites('Пробуждение Левиафана')
        assert len(book_shelf.get_list_of_favorites_books()) == 2

    #Тест добавляет в Избранное несуществующую книгу. Книга не будет добавлена
    def test_add_book_in_favorites_not_existing_book_should_not_add_to_favorites(self, book_shelf):
        book_shelf.add_book_in_favorites('Горе от ума')
        assert len(book_shelf.get_list_of_favorites_books()) == 0

    #Тест добавляет и удаляет книги из Избранного. В Избранном должна остаться только неудаленная книга.
    def test_delete_book_from_favorites_delete_one_book(self, book_shelf):
        book_shelf.add_book_in_favorites('Пробуждение Левиафана')
        book_shelf.add_book_in_favorites('Хребты безумия')
        book_shelf.delete_book_from_favorites('Пробуждение Левиафана')
        assert book_shelf.get_list_of_favorites_books() == ['Хребты безумия']

