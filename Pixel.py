class Pixel:
    def __init__(self, r : int, g : int, b : int) -> None:
        assert r <= 255 and r >= 0, "Value is out of range"
        assert g <= 255 and g >= 0, "Value is out of range"
        assert b <= 255 and b >= 0, "Value is out of range"

        self._r = r
        self._g = g
        self._b = b

    def getRed(self) -> int:
        return self._r

    def getGreen(self) -> int:
        return self._g

    def getBlue(self) -> int:
        return self._b

    def setRed(self, value : int) -> None:
        assert value <= 255 and value >= 0, "Value is out of range"
        self._r = value

    def setGreen(self, value : int) -> None:
        assert value <= 255 and value >= 0, "Value is out of range"
        self._g = value

    def setBlue(self, value : int) -> None:
        assert value <= 255 and value >= 0, "Value is out of range"
        self._b = value