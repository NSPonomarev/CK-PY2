import doctest


class CashMachine:
    def __init__(self, account: int):
        """
        Создание и подготовка к работе объекта "Банкомат"

        :param account: Сумма денег на счете

        Примеры:
        >>> money = CashMachine(5000)
        """

        if not isinstance(account, int):
            raise TypeError("Сумма денег на счете должна быть типа int")
        if account <= 0:
            raise ValueError("Сумма денег на счете должна быть положительным числом")
        self.account = account
        self.new_account = 0

    def to_withdraw(self, withdrawals: int) -> int:
        """
        Снятие со счета

        :param withdrawals: Сумма снятия
        :raise ValueError: Если сумма снятия превышает сумму денег на счете, то вызываем ошибку

        :return: Сумма денег на счете после снятия

        Примеры:
        >>> money = CashMachine(10000)
        >>> money.to_withdraw(6000)
        4000
        """

        if not isinstance(withdrawals, int):
            raise TypeError("Сумма снятия должна быть типа int")
        if not withdrawals >= 100 and withdrawals % 100 == 0:
            raise ValueError("Сумма снятия должна быть больше и кратна 100")
        if withdrawals > self.account:
            raise ValueError("Сумма снятия не должна превышать сумму денег на счете")
        self.account -= withdrawals
        return self.account

    def to_deposit(self, deposits: int) -> int:
        """
        Пополнение счета

        :param deposits: Сумма пополнения

        :return: Сумма денег на счете после пополнения

        Примеры:
        >>> money = CashMachine(9550)
        >>> money.to_deposit(1000)
        10550
        """

        if not isinstance(deposits, int):
            raise TypeError("Сумма пополнения должна быть типа int")
        if not deposits >= 100 and deposits % 100 == 0:
            raise ValueError("Сумма пополнения должна быть больше и кратна 100")
        self.account += deposits
        return self.account


class Calculator:
    def __init__(self, number_1: (int, float), number_2: (int, float)):
        """
        Создание и подготовка к работе объекта "Калькулятор"

        :param number_1: Первое число
        :param number_2: Второе число

        Примеры:
        >>> numbers = Calculator(1, 2)
        """

        if not isinstance(number_1, (int, float)):
            raise TypeError("Число должно быть типа int или float")
        self.number_1 = number_1

        if not isinstance(number_2, (int, float)):
            raise TypeError("Число должно быть типа int или float")
        self.number_2 = number_2

    def addition(self) -> (int, float):
        """
        Сложение

        :return: Сумма двух чисел

        Примеры:
        >>> numbers = Calculator(2, 2)
        >>> numbers.addition()
        4
        """

        return self.number_1 + self.number_2

    def subtraction(self) -> (int, float):
        """
        Вычитание

        :return: Разность двух чисел

        Примеры:
        >>> numbers = Calculator(0, 2)
        >>> numbers.subtraction()
        -2
        """

        return self.number_1 - self.number_2

    def multiplication(self) -> (int, float):
        """
        Умножение

        :return: Произведение двух чисел

        Примеры:
        >>> numbers = Calculator(5, 5)
        >>> numbers.multiplication()
        25
        """

        return self.number_1 * self.number_2

    def division(self) -> (int, float):
        """
        Деление

        :raise ValueError: При делении на ноль вызываем ошибку
        :return: Частное двух чисел

        Примеры:
        >>> numbers = Calculator(3, 5)
        >>> numbers.division()
        0.6
        """

        if self.number_2 == 0:
            raise ValueError("На ноль делить нельзя")
        return self.number_1 / self.number_2

    def exponentiation(self) -> (int, float):
        """
        Возведение в степень

        :return: Степень числа

        Примеры:
        >>> numbers = Calculator(2, 7)
        >>> numbers.exponentiation()
        128
        """

        return self.number_1 ** self.number_2


class SmartKettle:
    def __init__(self, water: int, start_temp: int):
        """
        Создание и подготовка к работе объекта "Умный чайник"

        :param water: Объем воды в чайнике
        :param start_temp: Начальная температура воды

        Примеры:
        >>> kettle = SmartKettle(1000, 25)
        """

        if not isinstance(water, int):
            raise TypeError("Объем воды должен быть типа int")
        if not 500 <= water <= 1500:
            raise ValueError("Объем воды должен быть в пределах 500 - 1500 мл")
        self.water = water

        if not isinstance(start_temp, int):
            raise TypeError("Начальная температура должна быть типа int")
        if not 0 < start_temp < 100:
            raise ValueError("Начальная температура должена быть в пределах 0 - 100 С")
        self.start_temp = start_temp

    def heat_up(self, final_temp: int) -> None:
        """
        Нагрев до заданной температуры

        :param final_temp: Конечная температура

        :return: Вода с заданной температурой

        Примеры:
        >>> kettle = SmartKettle(1500, 20)
        >>> kettle.heat_up(80)
        """

        if not isinstance(final_temp, int):
            raise TypeError("Конечная температура должна быть типа int")
        if not self.start_temp < final_temp and final_temp != 100:
            raise ValueError("Конечная температура должена быть выше начальной и не равна 100")
        ...

    def boil(self) -> None:
        """
        Кипячение воды

        :return: Кипяток

        Примеры:
        >>> kettle = SmartKettle(700, 50)
        >>> kettle.boil()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
#
