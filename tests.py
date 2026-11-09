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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
import unittest
from books_collector import BooksCollector

class TestBooksCollector(unittest.TestCase):
    
    def setUp(self):
        self.collector = BooksCollector()
    
    # Проверка добавления новой книги
    def test_add_new_book(self):
        self.collector.add_new_book("Война и мир")
        self.assertIn("Война и мир", self.collector.books_genre)
        self.assertEqual(self.collector.books_genre["Война и мир"], "")
        
        # Проверка на максимальную длину названия
        self.collector.add_new_book("A" * 40)
        self.assertIn("A" * 40, self.collector.books_genre)
        
        # Проверка на превышение максимальной длины
        self.collector.add_new_book("A" * 41)
        self.assertNotIn("A" * 41, self.collector.books_genre)
        
        # Проверка на добавление дубликата
        self.collector.add_new_book("Война и мир")
        self.assertEqual(len(self.collector.books_genre), 2)
    
    # Проверка установки жанра
    def test_set_book_genre(self):
        self.collector.add_new_book("Гарри Поттер")
        self.collector.set_book_genre("Гарри Поттер", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Гарри Поттер"), "Фантастика")
        
        # Проверка на неверный жанр
        self.collector.set_book_genre("Гарри Поттер", "Фэнтези")
        self.assertEqual(self.collector.get_book_genre("Гарри Поттер"), "Фантастика")
    
    # Проверка получения книг по жанру
    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_new_book("Книга2")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.collector.set_book_genre("Книга2", "Фантастика")
        
        result = self.collector.get_books_with_specific_genre("Фантастика")
        self.assertEqual(result, ["Книга1", "Книга2"])
    
    # Проверка книг для детей
    def test_get_books_for_children(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_new_book("Книга2")
        self.collector.set_book_genre("Книга1", "Мультфильмы")
        self.collector.set_book_genre("Книга2", "Ужасы")
        
        result = self.collector.get_books_for_children()
        self.assertEqual(result, ["Книга1"])
    
    # Проверка работы с избранным
    def test_favorites_functionality(self):
        self.collector.add_new_book("Любимая книга")
        self.collector.add_book_in_favorites("Любимая книга")
        self.assertIn("Любимая книга", self.collector.favorites)
        
        # Проверка на добавление дубликата
        self.collector.add_book_in_favorites("Любимая книга")
        self.assertEqual(len(self.collector.favorites), 1)
        
        # Проверка удаления
        self.collector.delete_book_from_favorites("Любимая книга")
        self.assertNotIn("Любимая книга", self.collector.favorites)

    # Дополнительные тесты
    def test_empty_book_genre(self):
        self.collector.add_new_book("Новая книга")
        self.assertEqual(self.collector.get_book_genre("Новая книга"), "")

    def test_non_existent_book(self):
        self.assertIsNone(self.collector.get_book_genre("Несуществующая книга"))
    
    def test_all_genres(self):
        for genre in self.collector.genre:
            self.collector.add_new_book(f"Книга {genre}")
            self.collector.set_book_genre(f"Книга {genre}", genre)
            self.assertEqual