def calculate_deposit(deposit_amount: float, deposit_term: int, rates_periods: list) -> float:
    total_interest: float = 0.0
    months_counted: int = 0

    for i, period in enumerate(rates_periods):
        rate: float = period['rate']

        if i < len(rates_periods) - 1:
            # Для всех периодов, кроме последнего
            months: int = period['months']
        else:
            # Для последнего периода используем весь оставшийся срок
            months = deposit_term - months_counted

        if deposit_term <= months_counted + months:
            # Если оставшийся срок вклада меньше, чем длительность текущего или последнего периода
            months_to_count = deposit_term - months_counted
            total_interest += deposit_amount * (rate / 12) * months_to_count
            break
        else:
            total_interest += deposit_amount * (rate / 12) * months
            months_counted += months

    return total_interest

# Ввод данных пользователем
deposit_amount: float = float(input("Введите сумму вклада: "))
deposit_term: int = int(input("Введите срок вклада в месяцах: "))

# Ввод информации о процентных ставках
rates_periods = []
periods_count: int = int(input("Введите количество периодов с разными процентными ставками: "))
for i in range(periods_count - 1):  # Запрашиваем данные для всех периодов, кроме последнего
    print(f"Период {i + 1}:")
    rate: float = float(input("Введите годовую процентную ставку (например, 15 для 15% годовых): ")) / 100
    months: int = int(input("Введите количество месяцев для этой ставки: "))
    rates_periods.append({'rate': rate, 'months': months})

# Добавляем последний период, для которого количество месяцев не требуется
print(f"Период {periods_count}:")
rate: float = float(input("Введите годовую процентную ставку для последнего периода (например, 15 для 15% годовых): ")) / 100
rates_periods.append({'rate': rate})

# Расчёт и вывод результатов
total_interest: float = calculate_deposit(deposit_amount, deposit_term, rates_periods)
print(f"Сумма процентов по вкладу составит: {total_interest:.2f}")
