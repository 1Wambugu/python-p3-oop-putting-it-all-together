import io
import sys
import unittest
from lib.book import Book

class TestBook(unittest.TestCase):
    def test_has_title_and_page_count(self):
        book = Book("And Then There Were None", 272)
        assert book.page_count == 272
        assert book.title == "And Then There Were None"

    def test_requires_int_page_count(self):
        book = Book("And Then There Were None", 272)
        with self.assertRaises(TypeError):
            book.page_count = "not an integer"

    def test_can_turn_page(self):
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
