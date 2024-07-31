import pytest
from main import BooksCollector


@pytest.fixture
def book_shelf():
    collector = BooksCollector()
    collector.add_new_book('Мечтают ли андроиды об электроовцах?')
    collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')
    collector.add_new_book('Пробуждение Левиафана')
    collector.set_book_genre('Пробуждение Левиафана', 'Фантастика')
    collector.add_new_book('Гнев Тиамат')
    collector.set_book_genre('Гнев Тиамат', 'Фантастика')
    collector.add_new_book('Цвет из иных миров')
    collector.set_book_genre('Цвет из иных миров', 'Фантастика')
    collector.add_new_book('Хребты безумия')
    collector.set_book_genre('Хребты безумия', 'Ужасы')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.add_new_book('Дракула')
    collector.set_book_genre('Дракула', 'Ужасы')
    collector.add_new_book('Снеговик')
    collector.set_book_genre('Снеговик', 'Детективы')
    collector.add_new_book('10 негритят')
    collector.set_book_genre('10 негритят', 'Детективы')
    collector.add_new_book('Холодное сердце')
    collector.set_book_genre('Холодное сердце', 'Мультфильмы')
    collector.add_new_book('Спящая красавица')
    collector.set_book_genre('Спящая красавица', 'Мультфильмы')
    collector.add_new_book('Мизантроп')
    collector.set_book_genre('Мизантроп', 'Комедии')
    collector.add_new_book('Похождения бравого солдата Швейка')
    collector.set_book_genre('Похождения бравого солдата Швейка', 'Комедии')
    return collector
