import matplotlib.pyplot as plt
from collections import defaultdict


# Функция read_sales_data читает данные из файла и возвращает список словарей с информацией о каждой продаже
def read_sales_data(file_path):
    sales = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            product_name, quantity_str, price_str, date = line.strip().split(', ')
            quantity = int(quantity_str)
            price = float(price_str)
            sales.append({
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'date': date
            })
    return sales


# Функция total_sales_per_product вычисляет общую сумму продаж для каждого продукта и возвращает словарь
def total_sales_per_product(sales_data):
    total_sales = defaultdict(float)
    for sale in sales_data:
        product_name = sale['product_name']
        total_sales[product_name] += sale['quantity'] * sale['price']
    return dict(total_sales)


# Функция sales_over_time вычисляет общую сумму продаж за каждый день и возвращает словарь
def sales_over_time(sales_data):
    sales_by_date = defaultdict(float)
    for sale in sales_data:
        date = sale['date']
        sales_by_date[date] += sale['quantity'] * sale['price']
    return dict(sales_by_date)


def main():
    # Путь к файлу с данными о продажах
    file_path = 'sales_data.txt'

    # Чтение данных о продажах
    sales_data = read_sales_data(file_path)

    # Общая сумма продаж по продуктам
    product_sales = total_sales_per_product(sales_data)

    # Определяем продукт с наибольшей выручкой
    max_product = max(product_sales.items(), key=lambda x: x[1])
    print(f"Продукт с наибольшей выручкой: {max_product[0]} - {max_product[1]:.2f} руб.")

    # Общая сумма продаж по дням
    daily_sales = sales_over_time(sales_data)

    # Определяем день с наибольшей суммой продаж
    max_date = max(daily_sales.items(), key=lambda x: x[1])
    print(f"День с наибольшей суммой продаж: {max_date[0]} - {max_date[1]:.2f} руб.")

    # Построение графика общей суммы продаж по каждому продукту
    plt.figure(figsize=(10, 5))
    plt.bar(product_sales.keys(), product_sales.values())
    plt.title('Общая сумма продаж по продуктам')
    plt.xlabel('Продукты')
    plt.ylabel('Сумма продаж (руб.)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Построение графика общей суммы продаж по дням
    plt.figure(figsize=(10, 5))
    plt.bar(daily_sales.keys(), daily_sales.values())
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Даты')
    plt.ylabel('Сумма продаж (руб.)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()