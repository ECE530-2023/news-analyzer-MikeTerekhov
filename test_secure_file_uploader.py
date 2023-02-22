import pytest

from secure_file_upload import * 

def test_checker_function():
    # assert checker("hi.LOL") == True
    assert checker("hi.txt") == True