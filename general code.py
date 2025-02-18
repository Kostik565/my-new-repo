from employeer import work_with_employees
from matrix import work_with_matrices
from vowels import find_vowels

def main():
    print("=== Робота зі співробітниками ===")
    work_with_employees()

    print("\n=== Робота з матрицями ===")
    a = int(input('Введіть кількість регіонів (рядків матриці): '))
    b = int(input('Введіть кількість років (стовпців матриці): '))
    work_with_matrices(a, b)

    print("\n=== Аналіз тексту ===")
    words = ["Тюлень", "Олень", "Ведмідь"]
    results = find_vowels(words)
    for word, percent in results.items():
        print(f"Відсоток голосних у слові '{word}': {percent:.2f}%")

if __name__ == "__main__":
    main()