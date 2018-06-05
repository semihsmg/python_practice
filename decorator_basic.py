def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def question_mark(func):
    def wrapper():
        return ' ?q? ' + func() + ' ?q? '

    return wrapper


def exclamation_mark(func):
    def wrapper():
        return ' !e! ' + func() + ' !e! '

    return wrapper


@exclamation_mark
@uppercase
@question_mark
def greet():
    return 'Hello!'


print(greet())
