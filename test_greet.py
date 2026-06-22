from greet import greet


def test_greet_returns_greeting():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_different_name():
    assert greet("World") == "Hello, World!"
