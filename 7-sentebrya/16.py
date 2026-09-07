import random

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
classes = [Line, Rect, Ellipse]
elements = []
for _ in range(217):
    cls = random.choice(classes)
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    d = random.randint(-100, 100)
    elements.append(cls(a, b, c, d))
for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)

print(f"Всего объектов: {len(elements)}")
line_count = sum(1 for obj in elements if isinstance(obj, Line))
rect_count = sum(1 for obj in elements if isinstance(obj, Rect))
ellipse_count = sum(1 for obj in elements if isinstance(obj, Ellipse))
print(f"Line: {line_count}, Rect: {rect_count}, Ellipse: {ellipse_count}")

print("\nПервые 5 объектов:")
for i, obj in enumerate(elements[:5]):
    print(f"{i}: {obj.__class__.__name__}, sp={obj.sp}, ep={obj.ep}")

all_zero = all(obj.sp == (0, 0) and obj.ep == (0, 0) for obj in elements if isinstance(obj, Line))
print(f"\nВсе Line обнулены? {all_zero}")