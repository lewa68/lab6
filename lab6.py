# Задание 1
class BigBell:
    def __init__(self):
        self.sounds = ["ding", "dong"]
        self.index = 0

    def sound(self):
        print(self.sounds[self.index % 2])
        self.index += 1


# Задание 2
class Balance:
    def __init__(self):
        self.left = self.right = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left == self.right:
            return "="
        return "L" if self.left > self.right else "R"


# Задание 3
class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [x for x in self.numbers if x % 2]

    def get_evens(self):
        return [x for x in self.numbers if not x % 2]


# Задание 4
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)


# Задание 5
class ReversedList:
    def init(self, original_list):
        self.original_list = original_list
    def len(self):
        return len(self.original_list)
    def getitem(self, index):
        if index < 0 or index >= len(self.original_list):
            raise IndexError("Index Error")
        return self.original_list[len(self.original_list) - 1 - index]
r1 = ReversedList([10, 20, 30])
print(len(r1))
for i in range(len(r1)):
    print(r1[i])
r2 = ReversedList([])
print(len(r2))

# Задание 6
class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data.get(key, 0)


# Задание 7
class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def __call__(self, x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(self.coeffs))

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = [
            (self.coeffs[i] if i < len(self.coeffs) else 0) +
            (other.coeffs[i] if i < len(other.coeffs) else 0)
            for i in range(max_len)
        ]
        return Polynomial(new_coeffs)


# Задание 8
class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        self.items.extend(values)

    def copy(self):
        return Queue(*self.items)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def extend(self, other):
        self.items.extend(other.items)

    def next(self):
        return Queue(*self.items[1:]) if len(self.items) > 1 else Queue()

    def __add__(self, other):
        return Queue(*(self.items + other.items))

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __rshift__(self, n):
        return Queue(*self.items[n:]) if n < len(self.items) else Queue()

    def __str__(self):
        return f"[{' -> '.join(map(str, self.items))}]" if self.items else "[]"

    __next__ = next


# Задание 9
class Triangle:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def perimeter(self):
        return sum(self.sides)


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


# Задание 10-11
class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)


# Задание 12
class A:
    def __str__(self):
        return 'A_str_method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B_str_method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    pass


# Задание 13
import math


class Weapon:
    def __init__(self, name, damage, range_):
        self.name, self.damage, self.range = name, damage, range_

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return

        ax, ay = actor.get_coords()
        tx, ty = target.get_coords()
        distance = math.hypot(ax - tx, ay - ty)

        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
            return

        print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
        target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y, self.hp = pos_x, pos_y, hp

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def get_coords(self):
        return (self.pos_x, self.pos_y)


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
            return
        self.weapon.hit(self, target)

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon = -1

    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
            return
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
            return
        self.weapons[self.current_weapon].hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return

        self.weapons.append(weapon)
        print(f"Подобрал {weapon}")
        if len(self.weapons) == 1:
            self.current_weapon = 0

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
        elif len(self.weapons) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
            print(f"Сменил оружие на {self.weapons[self.current_weapon]}")

    def heal(self, amount):
        self.hp = min(200, self.hp + amount)
        print(f"Полечился, теперь здоровья {self.hp}")


# Задание 15
commands = {
    'make_negative': (lambda x: x > 0, lambda x: -x),
    'square': (lambda _: True, lambda x: x ** 2),
    'strange_command': (lambda x: x % 5 == 0, lambda x: x + 1)
}

numbers = list(map(int, input().split()))
while (cmd := input().strip()) in commands:
    condition, transform = commands[cmd]
    numbers = [transform(x) if condition(x) else x for x in numbers]
    print(' '.join(map(str, numbers)))

    # Задание 16
    import math


class Function:
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    def __init__(self, name, left, op, right):
        self.name, self.left, self.op, self.right = name, left, op, right

    def evaluate(self, x):
        left = self.left if isinstance(self.left, (int, float)) else self.left.evaluate(x)
        right = self.right if isinstance(self.right, (int, float)) else self.right.evaluate(x)
        return self.ops[self.op](left, right)


x_func = Function('x', 0, '+', 0)
sqrt_func = Function('sqrt_fun', 0, '+', 0)

x_func.evaluate = lambda self, x: x
sqrt_func.evaluate = lambda self, x: math.sqrt(x)

functions = {'x': x_func, 'sqrt_fun': sqrt_func}

n = int(input())
for _ in range(n):
    parts = input().split()
    if not parts:
        continue

    if parts[0] == 'define':
        name, left, op, right = parts[1], parts[2], parts[3], parts[4]
        left_obj = float(left) if left.replace('.', '').isdigit() else functions.get(left)
        right_obj = float(right) if right.replace('.', '').isdigit() else functions.get(right)

        if None in (left_obj, right_obj):
            print("Unknown function in definition")
            continue

        functions[name] = Function(name, left_obj, op, right_obj)

    elif parts[0] == 'calculate':
        func = functions.get(parts[1])
        if not func:
            print("Unknown function")
            continue

        points = list(map(float, parts[2:]))
        results = [str(func.evaluate(p)) for p in points]
        print(' '.join(results))


# Задание 17
class Presentation:
    def __init__(self, topic, start, duration):
        self.topic, self.start, self.duration = topic, start, duration
        self.end = start + duration

    def overlaps(self, other):
        return not (self.end <= other.start or other.end <= self.start)


class Conference:
    def __init__(self):
        self.presentations = []

    def add_presentation(self, pres):
        if any(p.overlaps(pres) for p in self.presentations):
            print(f"Пересечение с другим докладом: {pres.topic}")
            return False
        self.presentations.append(pres)
        self.presentations.sort(key=lambda p: p.start)
        return True

    def total_duration(self):
        return sum(p.duration for p in self.presentations)

    def max_break(self):
        breaks = [self.presentations[i + 1].start - self.presentations[i].end
                  for i in range(len(self.presentations) - 1)]
        return max(breaks) if breaks else 0

    def print_schedule(self):
        for i, p in enumerate(self.presentations, 1):
            print(f"{i}. {p.topic} ({p.start}-{p.end})")
        print(f"Общая продолжительность: {self.total_duration()}")
        print(f"Максимальный перерыв: {self.max_break()}")


# Задание 18
class File:
    def __init__(self, name):
        self.name, self.content = name, ""

    def write(self, text):
        self.content = text

    def read(self):
        return self.content


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirs = {}

    def get_or_create_subdir(self, name):
        if name not in self.subdirs:
            self.subdirs[name] = Directory(name)
        return self.subdirs[name]

    def get_subdir(self, path):
        if not path:
            return self
        current = self
        for part in path:
            if part not in current.subdirs:
                return None
            current = current.subdirs[part]
        return current

    def list_contents(self):
        return list(self.subdirs.keys()) + list(self.files.keys())


class FileSystem:
    def __init__(self):
        self.root = Directory("")

    def _resolve_path(self, path):
        parts = path.split('/') if path else []
        dir_parts = parts[:-1] if '.' in parts[-1] else parts
        filename = parts[-1] if '.' in parts[-1] else None
        return dir_parts, filename

    def create_directory(self, path):
        parts = path.split('/') if path else []
        current = self.root
        for part in parts:
            current = current.get_or_create_subdir(part)

    def list_directory(self, path):
        dir_parts, _ = self._resolve_path(path)
        target = self.root.get_subdir(dir_parts)
        return target.list_contents() if target else []

    def write_file(self, path, content):
        dir_parts, filename = self._resolve_path(path)
        target = self.root.get_subdir(dir_parts)
        if target and filename:
            target.files[filename] = File(filename)
            target.files[filename].write(content)

    def read_file(self, path):
        dir_parts, filename = self._resolve_path(path)
        target = self.root.get_subdir(dir_parts)
        return target.files[filename].read() if target and filename in target.files else ""