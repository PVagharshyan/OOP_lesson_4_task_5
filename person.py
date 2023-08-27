class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, set_age: int) -> bool:
        if set_age <= 0:
            raise ValueError("Error: none valid age!")
        self._age = set_age
        return True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, set_name) -> None:
        self._name = set_name

def main() -> None:
    print("!person!")

if __name__ == "__main__":
    main()
