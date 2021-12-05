class SuperSample:
    def __init__(self):
        self._name = "hello"

    def get_name(self) -> str:
        return f"super {self._name}"


class Sample(SuperSample):
    def __init__(self):
        self._name = "world"
    
    def get_name(self) -> str:
        return f"{super().get_name()} sample"
