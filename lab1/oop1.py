class TransportError(Exception):
    pass

class OverbookingError(TransportError):
    def __init__(self, current: int, max_cap: int):
        super().__init__(f"нельзя добавить пассажиров занято {current}, максимум {max_cap}")

class InvalidSpeedError(TransportError):
    def __init__(self, speed: float):
        super().__init__(f"недопустимая скорость {speed}")

