import pytest

from secure_file_upload import * 
from nlp import *
from news_feed import *

# Unit tests for all API modules

class TestClass:

    # test_unit_tests.py

    def test_checker_function(self):
        assert checker("hi.LOL") == True
        assert checker("hi.txt") == True
    
    def test_secure_login(self):
        assert secure_login("Not Mike", 456) == True
        assert secure_login("Not Mike", 456) == False
        assert secure_login("Mike", 123) == True
        assert secure_login("", 0000) == True

    def test_uploader(self):
        assert uploader("image") == True
        assert uploader("file") == True
        assert uploader("Neither") == True

    # nlp.py

    def test_translater(self):
        assert translate("hi my name is Mike", 1, 2) == True
        assert translate("Same language?", 1, 1) == True

    def test_summary(self):
        assert summary("") == True
        assert summary("Sample Text") == True

    def test_sentiments(self):
        assert sentiments("") == True
        assert sentiments("Sample Text") == True

    def test_search_file(self):
        assert search_file("") == True
        assert search_file("dogs") == True

    def test_key_words(self):
        assert key_words("") == True
        assert key_words("dogs") == True

    # news_feed.py

    # for uploader and checker functions can reuse same test functions from secure_file_upload

    # def prese

    def test_presentation_interface(self):
        assert presentation_interface([sentiments, summary]) == True
        assert presentation_interface([]) == True
