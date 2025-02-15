class ConiferousTree:
    # хвойные деревья
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @property
    def age(self) -> int:
        return self._age

    def grow(self, growth: float) -> None:
        self._height += growth

    def shed_needles(self) -> None:
        # сброс хвои
        print(f"{self.name} сбрасывает хвою.")

    def __str__(self) -> str:
        return f"Хвойное дерево {self.name}. Высота: {self.height} м. Возраст: {self.age} лет."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height!r}, age={self.age!r})"


class Pine(ConiferousTree):

    def __init__(self, name: str, height: float, age: int, cone_count: int):
        super().__init__(name, height, age)
        self._cone_count = cone_count

    @property
    def cone_count(self) -> int:
        return self._cone_count

    @cone_count.setter
    def cone_count(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество шишек должно быть неотрицательным целым числом.")
        self._cone_count = value

    def produce_cones(self) -> None:
        # перегрузка shed_needles из базового класса
        print(f"{self.name} производит шишки.")

    def __str__(self) -> str:
        return f"Сосна {self.name}. Высота: {self.height} м. Возраст: {self.age} лет. Количество шишек: {self.cone_count}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height!r}, age={self.age!r}, cone_count={self.cone_count!r})"


class DeciduousTree:
    # лиственные деревья
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @property
    def age(self) -> int:
        return self._age

    def grow(self, growth: float) -> None:
        self._height += growth

    def shed_leaves(self) -> None:
        # сброс листвы
        print(f"{self.name} сбрасывает листья.")

    def __str__(self) -> str:
        return f"Лиственное дерево {self.name}. Высота: {self.height} м. Возраст: {self.age} лет."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height!r}, age={self.age!r})"


class Birch(DeciduousTree):

    def __init__(self, name: str, height: float, age: int, leaf_color: str):
        super().__init__(name, height, age)
        self._leaf_color = leaf_color

    @property
    def leaf_color(self) -> str:
        return self._leaf_color

    @leaf_color.setter
    def leaf_color(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Это вам не RGB, должны быть буквы!")
        self._leaf_color = value

    def change_leaf_color(self, new_color: str) -> None:
        # перегрузка shed_leaves
        self.leaf_color = new_color
        print(f"Цвет листьев {self.name} изменился на {self.leaf_color}.")

    def __str__(self) -> str:
        return f"Береза {self.name}. Высота: {self.height} м. Возраст: {self.age} лет. Цвет листьев: {self.leaf_color}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height!r}, age={self.age!r}, leaf_color={self.leaf_color!r})"


if __name__ == "__main__":
    pine = Pine(name="Сосна", height=15.0, age=20, cone_count=50)
    print(pine)
    pine.grow(2.5)
    pine.produce_cones()

    birch = Birch(name="Береза", height=10.0, age=15, leaf_color="зеленый")
    print(birch)
    birch.grow(1.5)
    birch.change_leaf_color("желтый")
