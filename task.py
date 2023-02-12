if __name__ == "__main__":
    class Work:
        def __init__(self, name: str, rate: int, hours: int):
            """
            Инициализация базового класса

            :param name: Имя сотрудника
            :param rate: Тарифная ставка
            :param hours: Время работы
            """

            self.name = name
            self._rate = rate  # тарифную ставку изменять нельзя
            self.hours = hours

        @property
        def rate(self) -> int:
            return self._rate

        def __str__(self) -> str:
            return f"Сотрудник {self.name}. Ставка {self.rate}. Часы {self.hours}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, rate={self.rate}, hours={self.hours}"

        def pay(self) -> int:
            """
            Расчет зарплаты

            :return: Размер зарплаты
            """

            return self.rate * self.hours

        def promotion(self) -> None:
            """
            Повышение в должности

            :return None
            """

    class Overtime(Work):
        def __init__(self, name: str, rate: int, hours: int, extra: int):
            """
            Инициализация дочернего класса

            :param extra: Сверхурочное время
            """

            super().__init__(name, rate, hours)
            self.extra = extra

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, rate={self.rate}, hours={self.hours}, extra={self.extra})"

        def pay(self) -> int:
            """
            Расчет зарплаты с учетом сверхурочных

            :return: Пересчитанный размер зарплаты
            """

            return super().pay() + 2 * self.rate * self.extra
    pass
#
