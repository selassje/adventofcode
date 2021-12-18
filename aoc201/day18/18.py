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
        left.__parent = number
        right.__parent = number
        return number

    def __init__(self, create_key) -> None:
        assert (
            create_key == SnailFishNumber.__create_key
        ), "OnlyCreatable objects must be created using OnlyCreatable.create"
        self.__value = None
        self.__left = None
        self.__right = None
        self.__parent = None

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

    def __add_to_closest(self, v, left):
        if self.__parent is None:
            return
        if left and self.__parent.__right == self:
            return self.__parent.__left.__add_to_next(v, False)

        if not left and self.__parent.__left == self:
            return self.__parent.__right.__add_to_next(v, True)

        self.__parent.__add_to_closest(v, left)

    def __add_to_next(self, v, left):
        if self.__value is not None:
            self.__value += v
        else:
            if left:
                self.__left.__add_to_next(v, left)
            else:
                self.__right.__add_to_next(v, left)

    def __explode(self, depth):
        if depth == 4 and self.get_value() is None:
            l = self.__left.get_value()
            r = self.__right.get_value()
            if l is not None and r is not None:
                self.__left = None
                self.__right = None
                self.__value = 0
                self.__add_to_closest(l, True)
                self.__add_to_closest(r, False)
                return True
        result = False
        if self.__left is not None:
            result = self.__left.__explode(depth + 1)
        if not result and self.__right is not None:
            result = self.__right.__explode(depth + 1)
        return result

    def explode(self):
        return self.__explode(0)


def split(number):
    return False


def add(number_1, number_2):
    added = SnailFishNumber.create_pair(number_1, number_2)
    while True:
        if added.explode():
            continue
        if split(added):
            continue
        break
    return added


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


def test_parse(number_str):
    number = parse(number_str)
    assert number_str == str(number)


def test_explode(number_str, expected_str):
    number = parse(number_str)
    was_exploded = number.explode()
    assert expected_str == str(number)
    assert not was_exploded == (number_str == expected_str)


f = open("example.txt")
numbers = []
for line in f.readlines():
    line = line.strip()
    test_parse(line)
    numbers.append(parse(line))


test_explode("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]")
test_explode("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]")
test_explode("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]")
test_explode(
    "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
)
test_explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

sum = numbers[0]
for number in numbers[1:]:
    sum = add(sum, number)
