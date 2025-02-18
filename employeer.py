class Співробітник:
    """Клас для представлення співробітника"""
    def __init__(self, прізвище, імя, вік, посада, зарплатня):
        self.прізвище = прізвище
        self.імя = імя
        self.вік = вік
        self.посада = посада
        self.зарплатня = зарплатня

def employee():
    """Створює та повертає словник співробітників"""
    return {
        "Петренко Іван": Співробітник("Петренко", "Іван", 23, "Аналітик", 12000),
        "Петренко Василь": Співробітник("Петренко", "Василь", 28, "Менеджер", 15000),
        "Сидоров Михайло": Співробітник("Сидоров", "Михайло", 35, "Дизайнер", 14000),
        "Коваленко Олексій": Співробітник("Коваленко", "Олексій", 29, "Розробник", 16000),
        "Панфілова Марія": Співробітник("Панфілова", "Марія", 25, "Тестувальник", 11000),
    }

def work_with_employees():
    workers = employee()
    
    print("\nПочатковий список співробітників:")
    for key, value in workers.items():
        print(f"{key}: {value.прізвище} {value.імя}, Вік: {value.вік}, Посада: {value.посада}, Зарплата: {value.зарплатня}")

    # Додаємо нових співробітників
    workers["Семенов Семен"] = Співробітник("Семенов", "Семен", 32, "Програміст", 17000)
    workers["Панфілова Анна"] = Співробітник("Панфілова", "Анна", 40, "Керівник", 20000)

    print("\nСписок пілсля нових співробітників")
    for key, value in workers.items():
        print(f"{key}: {value.прізвище} {value.імя}, Вік: {value.вік}, Посада: {value.посада}, Зарплата: {value.зарплатня}")

    print(f"\nЄмність колекції: {len(workers)}")

    workers.pop("Петренко Іван", None)
    workers.pop("Петренко Василь", None)
    print("\nОновлений список співробітників:")
    for key, value in workers.items():
        print(f"{key}: {value.прізвище} {value.імя}, Вік: {value.вік}, Посада: {value.посада}, Зарплата: {value.зарплатня}")

    print("\nПрограмісти:")
    for key, worker in workers.items():
        if worker.посада == "Програміст":
            print(f"{key}: {worker.прізвище} {worker.імя}, Вік: {worker.вік}, Посада: {worker.посада}, Зарплата: {worker.зарплатня}")