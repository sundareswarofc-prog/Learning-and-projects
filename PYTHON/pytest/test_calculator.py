from calculator import add as ad,sub
import pytest
def  test_add():
    assert ad(2,1)==3

def  test_sub():
    assert sub(2,1)==1


################################################################

@pytest.fixture
def marks():
    return [1,2,3,4,5]

def test_add(marks):
    assert sum(marks)==1

    

# How does this work?
# 1. Pytest sees @pytest.fixture.
# 2. It recognizes marks as a fixture.
# 3. The test requests marks as a function parameter.
# 4. Pytest runs the fixture and passes its returned value into the test.




