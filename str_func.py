def upper_string(text):
    """ФУНКЦИЯ ВЫВОДИТ СТРОКУ СО ВСЕМИ ЗАГЛАВНЫМИ БУКВАМИ"""
    return text.upper()


def capitalize_words(string):
    """Делает заглавными первые буквы каждого слова"""
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
