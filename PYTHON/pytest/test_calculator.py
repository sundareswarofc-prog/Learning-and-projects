import pytest
# from calculator import add as ad,sub
# import pytest
# def  test_add():
#     assert ad(2,1)==3

# def  test_sub():
#     assert sub(2,1)==1


################################################################

# @pytest.fixture
# def marks():
#     return [1,2,3,4,5]

# def test_add(marks):
#     assert sum(marks)==1

def calculate_total(price, quantity):
    return price * quantity


# def test_calculate_total():
#     result = calculate_total(100, 5)

#     assert result == 500

#     result_2=calculate_total(200, 0)
#     assert result_2 == 0



### From the above we pass the args seperately, To test all at once means we need to use the pytest decorator

@pytest.mark.parametrize("price,quantity,expect",[
    (100,2,200),
    (200,2,400)
])

def test_calculate_total(price,quantity,expect):
    result=calculate_total(price,quantity)
    assert result==expect



######## test for api ##################

# from fastapi.testclient import TestClient
# from main import app

# @pytest.fixture
# def client():
#     return TestClient(app)


# def test_home(client):
#     response = client.get("/")
#     assert response.status_code == 200




    

# How does this work?
# 1. Pytest sees @pytest.fixture.
# 2. It recognizes marks as a fixture.
# 3. The test requests marks as a function parameter.
# 4. Pytest runs the fixture and passes its returned value into the test.




