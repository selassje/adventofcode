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

    def get_magnitude(self):
        if self.__left is None and self.__right == None:
            assert self.__value is not None
            return self.__value
        return 3 * self.__left.get_magnitude() + 2 * self.__right.get_magnitude()

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
        if depth == 4 and self.__value is None:
            l = self.__left.__value
            r = self.__right.__value
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

    def split(self):
        if self.__value is not None and self.__value >= 10:
            l = int(self.__value / 2)
            if self.__value % 2 == 0:
                r = l
            else:
                r = l + 1
            self.__value = None
            self.__left = SnailFishNumber.create_single(l)
            self.__right = SnailFishNumber.create_single(r)
            self.__left.__parent = self
            self.__right.__parent = self
            return True

        result = False
        if self.__left is not None:
            result = self.__left.split()
        if not result and self.__right is not None:
            result = self.__right.split()
        return result

    def explode(self):
        return self.__explode(0)


def add(number_1, number_2):
    added = SnailFishNumber.create_pair(number_1, number_2)
    while True:
        # print(added)
        if added.explode():
            #   print("after explode")
            continue
        if added.split():
            #  print("after split")
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


def test_add(number1_str, number2_str, expected_str):
    number1 = parse(number1_str)
    number2 = parse(number2_str)
    added = add(number1, number2)
    assert expected_str == str(added)


f = open("input.txt")
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

test_add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
test_add(
    "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
    "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
)

sum = numbers[0]
for number in numbers[1:]:
    sum = add(sum, number)

print(sum.get_magnitude())
