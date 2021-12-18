import re


class SnailFishNumber(object):
    __create_key = object()

    @classmethod
    def create_single(cls, value):
        number = SnailFishNumber(cls.__create_key)
        number.__value = value
        return number

    @classmethod
    def create_pair(cls, left, right):
        number = SnailFishNumber(cls.__create_key)
        assert left is not None
        assert right is not None
        number.__left = left
        number.__right = right
        return number

    def __init__(self, create_key) -> None:
        assert (
            create_key == SnailFishNumber.__create_key
        ), "OnlyCreatable objects must be created using OnlyCreatable.create"
        self.__value = None
        self.__left = None
        self.__right = None

    def get_value(self):
        if self.__left is None and self.__right == None:
            assert self.__value is not None
            return self.__value
        return None

    def __str__(self) -> str:
        if self.__value is not None:
            return str(self.__value)
        else:
            return r"[{0},{1}]".format(str(self.__left), str(self.__right))


def parse(number_str):
    m = re.match(r"^(\d+)$", number_str)
    if m is not None:
        return SnailFishNumber.create_single(int(m.group(1)))
    braces = 0

    for i, c in enumerate(number_str[1:-2]):
        if c == "[":
            braces += 1
        if c == "]":
            braces -= 1
        if c == "," and braces == 0:
            return SnailFishNumber.create_pair(
                parse(number_str[1 : i + 1]), parse(number_str[i + 2 : -1])
            )
    raise RuntimeError("Parsing failed: " + number_str)


f = open("example.txt")
numbers = []
for line in f.readlines():
    n = parse(line.strip())
    print(n)
