def upper_string(text):
    """Функция выводит строку со всеми заглавными буквами"""
    return text.upper()


def capitalize_words(string):
    """Делает заглавными первые буквы каждого слова"""
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
