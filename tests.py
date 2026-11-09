import unittest
from main import BooksCollector


class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        # в каждом тесте создается свой экземпляр — тесты независимы
        self.collector = BooksCollector()

    # --- add_new_book ---

    def test_add_new_book_add_two_books(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.assertEqual(len(self.collector.get_books_genre()), 2)

    def test_add_new_book_max_length_name_added(self):
        self.collector.add_new_book('А' * 40)
        self.assertIn('А' * 40, self.collector.get_books_genre())

    def test_add_new_book_too_long_name_not_added(self):
        self.collector.add_new_book('А' * 41)
        self.assertNotIn('А' * 41, self.collector.get_books_genre())

    def test_add_new_book_duplicate_not_added(self):
        self.collector.add_new_book('Война и мир')
        self.collector.add_new_book('Война и мир')
        self.assertEqual(len(self.collector.get_books_genre()), 1)

    def test_add_new_book_genre_empty_by_default(self):
        self.collector.add_new_book('Война и мир')
        self.assertEqual(self.collector.get_book_genre('Война и мир'), '')

    # --- set_book_genre ---

    def test_set_book_genre_valid_genre(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фантастика')
        self.assertEqual(self.collector.get_book_genre('Гарри Поттер'), 'Фантастика')

    def test_set_book_genre_invalid_genre_ignored(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        self.assertEqual(self.collector.get_book_genre('Гарри Поттер'), '')

    def test_set_book_genre_non_existent_book(self):
        self.collector.set_book_genre('Несуществующая книга', 'Фантастика')
        self.assertNotIn('Несуществующая книга', self.collector.get_books_genre())

    # --- get_book_genre ---

    def test_get_book_genre_non_existent_book(self):
        self.assertIsNone(self.collector.get_book_genre('Несуществующая книга'))

    # --- get_books_with_specific_genre ---

    def test_get_books_with_specific_genre_returns_only_matching(self):
        self.collector.add_new_book('Книга1')
        self.collector.add_new_book('Книга2')
        self.collector.add_new_book('Книга3')
        self.collector.set_book_genre('Книга1', 'Фантастика')
        self.collector.set_book_genre('Книга2', 'Фантастика')
        self.collector.set_book_genre('Книга3', 'Ужасы')
        self.assertEqual(
            self.collector.get_books_with_specific_genre('Фантастика'),
            ['Книга1', 'Книга2']
        )

    def test_get_books_with_specific_genre_non_existent_genre(self):
        self.assertEqual(self.collector.get_books_with_specific_genre('Такого жанра нет'), [])

    # --- get_books_for_children ---

    def test_get_books_for_children_excludes_age_rated(self):
        self.collector.add_new_book('Мультфильм')
        self.collector.add_new_book('Ужасы-книга')
        self.collector.set_book_genre('Мультфильм', 'Мультфильмы')
        self.collector.set_book_genre('Ужасы-книга', 'Ужасы')
        self.assertEqual(self.collector.get_books_for_children(), ['Мультфильм'])

    def test_get_books_for_children_ignores_books_without_genre(self):
        self.collector.add_new_book('Книга без жанра')
        self.assertEqual(self.collector.get_books_for_children(), [])

    # --- add_book_in_favorites ---

    def test_add_book_in_favorites(self):
        self.collector.add_new_book('Любимая книга')
        self.collector.add_book_in_favorites('Любимая книга')
        self.assertIn('Любимая книга', self.collector.get_list_of_favorites_books())

    def test_add_book_in_favorites_duplicate_not_added(self):
        self.collector.add_new_book('Любимая книга')
        self.collector.add_book_in_favorites('Любимая книга')
        self.collector.add_book_in_favorites('Любимая книга')
        self.assertEqual(len(self.collector.get_list_of_favorites_books()), 1)

    def test_add_book_in_favorites_non_existent_book(self):
        self.collector.add_book_in_favorites('Несуществующая книга')
        self.assertEqual(self.collector.get_list_of_favorites_books(), [])

    # --- delete_book_from_favorites ---

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book('Любимая книга')
        self.collector.add_book_in_favorites('Любимая книга')
        self.collector.delete_book_from_favorites('Любимая книга')
        self.assertNotIn('Любимая книга', self.collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites_not_in_list(self):
        # удаление книги, которой нет в избранном, не ломает код
        self.collector.delete_book_from_favorites('Несуществующая книга')
        self.assertEqual(self.collector.get_list_of_favorites_books(), [])

    # --- get_list_of_favorites_books ---

    def test_get_list_of_favorites_books_empty_by_default(self):
        self.assertEqual(self.collector.get_list_of_favorites_books(), [])