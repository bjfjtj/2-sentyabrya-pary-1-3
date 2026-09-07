class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1000):
    x = 1 + 2 * i
    y = 1 + 2 * i
    if i == 1: 
        p = Point(x, y, 'yellow')
    else:
        p = Point(x, y)
    points.append(p)
print(points[0].x, points[0].y, points[0].color)
print(points[1].x, points[1].y, points[1].color)
print(points[2].x, points[2].y, points[2].color) 
print(len(points))