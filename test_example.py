from example import add, subtract

def test_add():
    assert add(0,0) == 0
    assert add(2,3) == 5
    assert add(-2,-3) == -5
    assert add(-2,3) == 1

def test_subtract():
    assert add(0,0) == 0
    assert subtract(1,0) == 1
    assert subtract(3,2) == 1
    
