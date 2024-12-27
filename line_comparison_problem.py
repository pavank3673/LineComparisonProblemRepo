from math import sqrt

print("Welcome to Line Comparison Computation Program")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def __str__(self):
        return f"Line with Point 1 co-ordinates : ({self.point_one.x}, {self.point_one.y}) & Point 2 co-ordinates : ({self.point_two.x}, {self.point_two.y})"

    def calculate_length(self):
        return sqrt(((self.point_two.x - self.point_one.x) ** 2) + ((self.point_two.y - self.point_one.y) ** 2))

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.calculate_length() == value.calculate_length()
        else:
            return False

    def __gt__(self, value):
        if isinstance(value, self.__class__):
            return self.calculate_length() > value.calculate_length()
        else:
            return False

    def __lt__(self, value):
        if isinstance(value, self.__class__):
            return self.calculate_length() < value.calculate_length()
        else:
            return False

    def compare_to(self, value):
        return ((self > value) - (self < value))


sample_line = Line(Point(1, 1), Point(3, 3))

print(sample_line)

sample_line_length = sample_line.calculate_length()

print(f"The length of line with co-ordinates ({sample_line.point_one.x}, {sample_line.point_one.y}) & ({sample_line.point_two.x}, {sample_line.point_two.y}) = {sample_line_length}")

sample_line_two = Line(Point(1, 1), Point(3, 3))
line_equals = sample_line == sample_line_two

if line_equals:
    print(f"The two lines with co-ordinates of Line 1, Point 1({sample_line.point_one.x}, {sample_line.point_one.y}) & Point 2({sample_line.point_two.x}, {sample_line.point_two.y}) and Line 2 Point 1({sample_line_two.point_one.x}, {sample_line_two.point_one.y}) & Point 2({sample_line_two.point_two.x}, {sample_line_two.point_two.y}) are equal")
else:
    print(f"The two lines with co-ordinates of Line 1, Point 1({sample_line.point_one.x}, {sample_line.point_one.y}) & Point 2({sample_line.point_two.x}, {sample_line.point_two.y}) and Line 2 Point 1({sample_line_two.point_one.x}, {sample_line_two.point_one.y}) & Point 2({sample_line_two.point_two.x}, {sample_line_two.point_two.y}) are not equal")


comparable_line_one = Line(Point(1, 1), Point(3, 3))
comparable_line_two = Line(Point(0, 1), Point(4, 4))
comparable_result = comparable_line_one.compare_to(comparable_line_two)

if comparable_result > 0:
    print(f"The Line with co-ordinates (({comparable_line_one.point_one.x}, {comparable_line_one.point_one.y}), ({comparable_line_one.point_two.x}, {comparable_line_one.point_two.y})) is greater than Line with co-ordinates (({comparable_line_two.point_one.x}, {comparable_line_two.point_one.y}), ({comparable_line_two.point_two.x}, {comparable_line_two.point_two.y}))")
elif comparable_result < 0:
    print(f"The Line with co-ordinates (({comparable_line_one.point_one.x}, {comparable_line_one.point_one.y}), ({comparable_line_one.point_two.x}, {comparable_line_one.point_two.y})) is less than Line with co-ordinates (({comparable_line_two.point_one.x}, {comparable_line_two.point_one.y}), ({comparable_line_two.point_two.x}, {comparable_line_two.point_two.y}))")
else:
    print(f"The Line with co-ordinates (({comparable_line_one.point_one.x}, {comparable_line_one.point_one.y}), ({comparable_line_one.point_two.x}, {comparable_line_one.point_two.y})) is equal to Line with co-ordinates (({comparable_line_two.point_one.x}, {comparable_line_two.point_one.y}), ({comparable_line_two.point_two.x}, {comparable_line_two.point_two.y}))")