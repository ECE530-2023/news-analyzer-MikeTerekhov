import pytest

from secure_file_upload import * 

class TestClass:

    def test_checker_function(self):
        assert checker("hi.LOL") == True
        assert checker("hi.txt") == True
    
    def test_secure_login(self):
        assert secure_login("Not Mike", 456) == True
        assert secure_login("Not Mike", 456) == False
        assert secure_login("Mike", 123) == True
        assert secure_login("", 0000) == True