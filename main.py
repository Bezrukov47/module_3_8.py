# Дополнительное практическое задание по модулю: "Подробнее о функциях."
def calculate_structure_sum(data):
    total_sum = 0
    for item in data:  # Проходим по каждому элементу в структуре
        if isinstance(item, (int, float)):  # Проверка на число
            total_sum += item  # Если это число, добавляем его к сумме
        elif isinstance(item, str):  # Проверка на строку
            total_sum += len(item)  # Если это строка, добавляем её длину
        elif isinstance(item, (list, tuple, set)):  # Проверка на коллекции
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для вложенных структур
        elif isinstance(item, dict):  # Проверка на словарь
            total_sum += calculate_structure_sum(item.keys())  # Суммируем ключи
            total_sum += calculate_structure_sum(item.values())  # Суммируем значения

    return total_sum  # Возвращаем общую сумму

data_structure= [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)