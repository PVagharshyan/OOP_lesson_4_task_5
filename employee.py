import person

class Employee(person.Person):
    _id: int = 0
    def __init__(self, name: str, age: int, department: str) -> None:
        super().__init__(name, age)
        self._current_id = self.get_id()
        self._department = department
        self.inc_id()

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, age: {self.age}, department: {self.department}\n"

    @classmethod
    def get_id(cls) -> int:
        return cls._id

    @classmethod
    def inc_id(cls) -> None:
        cls._id += 1

    @property
    def id(self) -> int:
        return self._current_id

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, set_department: str) -> None:
        self._department = set_department

def main() -> None:
    print("!employee!")

if __name__ == "__main__":
    main()
