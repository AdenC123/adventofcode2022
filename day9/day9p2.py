prog = []

with open('input.txt') as f:
    for line in f:
        direction, num = line.strip().split()
        prog.append((direction, int(num)))

print(prog)


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y

    def move(self, dir):
        # move head
        match dir:
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1

    def follow(self, tail, dir):
        if self.far(tail):
            match dir:
                case 'R':
                    tail.replace(Pos(self.x - 1, self.y))
                case 'L':
                    tail.replace(Pos(self.x + 1, self.y))
                case 'U':
                    tail.replace(Pos(self.x, self.y - 1))
                case 'D':
                    tail.replace(Pos(self.x, self.y + 1))
                case 'UR':
                    tail.replace(Pos(self.x - 1, self.y - 1))
                case 'UL':
                    tail.replace(Pos(self.x + 1, self.y - 1))
                case 'DR':
                    tail.replace(Pos(self.x - 1, self.y + 1))
                case 'DL':
                    tail.replace(Pos(self.x + 1, self.y + 1))

    def far(self, tail):
        # return abs(self.x - tail.x) > 1 or abs(self.y - tail.y) > 1
        if self.distance(tail) == (2, 2):
            return 'UR'
        elif self.distance(tail) == (-2, 2):
            return 'UL'
        elif self.distance(tail) == (2, -2):
            return 'DR'
        elif self.distance(tail) == (-2, -2):
            return 'DL'
        elif self.y - tail.y > 1:
            return 'U'
        elif self.y - tail.y < -1:
            return 'D'
        elif self.x - tail.x > 1:
            return 'R'
        elif self.x - tail.x < -1:
            return 'L'

        return False

    def distance(self, tail):
        return self.x - tail.x, self.y - tail.y

    def replace(self, pos):
        self.x = pos.x
        self.y = pos.y

    def multifollow(self, lok):
        if len(lok) == 0:
            return
        tail = lok[0]
        new_dir = self.far(tail)
        if not new_dir:
            return
        self.follow(tail, new_dir)
        tail.multifollow(lok[1:])



knots = []
for _ in range(10):
    knots.append(Pos(0, 0))

head = knots[0]
tail = knots[9]

tail_visited = set()
for ins in prog:
    dir, times = ins
    for _ in range(times):
        head.move(dir)
        head.multifollow(knots[1:])
        tail_visited.add((tail.x, tail.y))

for i in range(10):
    print(i, knots[i])
print(len(tail_visited))
print(tail_visited)
