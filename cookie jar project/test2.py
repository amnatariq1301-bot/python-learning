import pytest
from test import jar
def test_init():
    # Test default initialization
    jar = jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom valid initialization
    custom_jar = jar(5)
    assert custom_jar.capacity == 5
    assert custom_jar.size == 0

    # Test invalid initializations
    with pytest.raises(ValueError):
        jar(-1)
    with pytest.raises(ValueError):
        jar("ten")


def test_str():
    jar = jar()
    assert str(jar) == ""
    
    jar.deposit(1)
    assert str(jar) == "🍪"
    
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = jar(10)
    
    jar.deposit(5)
    assert jar.size == 5
    
    jar.deposit(5)
    assert jar.size == 10
    
    # Test depositing over capacity limits
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = jar(10)
    jar.deposit(8)
    
    jar.withdraw(3)
    assert jar.size == 5
    
    jar.withdraw(5)
    assert jar.size == 0
    
    # Test withdrawing more cookies than available
    with pytest.raises(ValueError):
        jar.withdraw(1)