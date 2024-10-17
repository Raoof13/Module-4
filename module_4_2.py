

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
# inner_function() # Если вызвать inner_function() вне test_function() выйдет ошибка "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
test_function()