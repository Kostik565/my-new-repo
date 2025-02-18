def find_percent(text):
    """Обчислює відсоток голосних у тексті"""
    v = {'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}
    N = len(text.replace(' ', ''))  
    if N == 0:
        return 0 
    v_count = sum(1 for i in text if i in v) 
    return (v_count / N) * 100 

def find_vowels(words):
    """Обчислює відсоток голосних у списку слів"""
    results = {word: find_percent(word) for word in words}
    return results