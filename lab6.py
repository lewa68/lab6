# Задание 1


class BigBell:
    def __init__(self):
        self.next_sound = "ding"

    def sound(self):
        print(self.next_sound)
        self.next_sound = "dong" if self.next_sound == "ding" else "ding"


# Задание 2
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left == self.right:
            return "="
        elif self.left > self.right:
            return "L"
        else:
            return "R"


# Задание 3
class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [x for x in self.numbers if x % 2 != 0]

    def get_evens(self):
        return [x for x in self.numbers if x % 2 == 0]


# Задание 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


# Задание 5


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if other.numerator == 0:
            raise ValueError("Деление на ноль невозможно.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


# Задание 6
class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data.get(index, 0)


# Задание 7
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coeff1 + coeff2)
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

    def extend(self, queue):
        self.items.extend(queue.items)

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
        return "[" + " -> ".join(map(str, self.items)) + "]" if self.items else "[]"

    def __next__(self):
        return self.next()


# Задание 9
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


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


class Weapon:
    def __init__(self, name, damage, range_):
        self.name = name
        self.damage = damage
        self.range = range_

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return

        actor_x, actor_y = actor.get_coords()
        target_x, target_y = target.get_coords()
        distance = math.sqrt((actor_x - target_x) ** 2 + (actor_y - target_y) ** 2)

        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
            return

        print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
        target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

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
        self.current_weapon_index = -1

    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
            return

        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
            return

        self.weapons[self.current_weapon_index].hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return

        self.weapons.append(weapon)
        print(f"Подобрал {weapon}")

        if len(self.weapons) == 1:
            self.current_weapon_index = 0

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
            return

        if len(self.weapons) == 1:
            print("У меня только одно оружие")
            return

        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
        print(f"Сменил оружие на {self.weapons[self.current_weapon_index]}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")


# Задание 14
class MailServer:
    _servers = {}

    def __init__(self, name):
        self.name = name
        self.mailboxes = {}
        self._servers[name] = self

    @classmethod
    def get_server(cls, name):
        return cls._servers.get(name)

    @classmethod
    def list_servers(cls):
        return list(cls._servers.keys())

    def add_user(self, user):
        if user not in self.mailboxes:
            self.mailboxes[user] = []

    def receive_mail(self, user, message):
        if user in self.mailboxes:
            self.mailboxes[user].append(message)
        else:
            raise ValueError(f"User {user} not found")

    def get_mail(self, user):
        if user in self.mailboxes:
            messages = self.mailboxes[user].copy()
            self.mailboxes[user].clear()
            return messages
        raise ValueError(f"User {user} not found")


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.server.add_user(user)

    def receive_mail(self):
        messages = self.server.get_mail(self.user)
        return messages if messages else "No new messages"

    def send_mail(self, target_server_name, target_user, message):
        target_server = MailServer.get_server(target_server_name)
        if not target_server:
            raise ValueError(f"Server {target_server_name} doesn't exist")
        target_server.receive_mail(target_user, message)
        return f"Message sent to {target_user}@{target_server_name}"


def main():
    print("Mail System Simulator")
    print("Available commands:")
    print("1. create_server <name>")
    print("2. create_user <server> <username>")
    print("3. send <from_user> <from_server> <to_user> <to_server> <message>")
    print("4. receive <user> <server>")
    print("5. list_servers")
    print("6. exit")

    while True:
        try:
            cmd = input("\n> ").strip().split()
            if not cmd:
                continue

            if cmd[0] == "create_server":
                MailServer(cmd[1])
                print(f"Server {cmd[1]} created")

            elif cmd[0] == "create_user":
                server = MailServer.get_server(cmd[1])
                if server:
                    MailClient(server, cmd[2])
                    print(f"User {cmd[2]} added to {cmd[1]}")
                else:
                    print("Server not found")

            elif cmd[0] == "send":
                server = MailServer.get_server(cmd[2])
                if server:
                    client = MailClient(server, cmd[1])
                    print(client.send_mail(cmd[4], cmd[3], ' '.join(cmd[5:])))
                else:
                    print("Source server not found")

            elif cmd[0] == "receive":
                server = MailServer.get_server(cmd[2])
                if server:
                    client = MailClient(server, cmd[1])
                    messages = client.receive_mail()
                    print("Received messages:" if isinstance(messages, list) else messages)
                    if isinstance(messages, list):
                        for msg in messages:
                            print(f"- {msg}")
                else:
                    print("Server not found")

            elif cmd[0] == "list_servers":
                servers = MailServer.list_servers()
                print("Available servers:", ', '.join(servers) if servers else "None")

            elif cmd[0] == "exit":
                break

            else:
                print("Unknown command")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


# Задание 15
def make_negative(x):
    return -x if x > 0 else x


def square(x):
    return x ** 2


def strange_command(x):
    return x + 1 if x % 5 == 0 else x


commands = {
    'make_negative': (lambda x: x > 0, make_negative),
    'square': (lambda x: True, square),
    'strange_command': (lambda x: x % 5 == 0, strange_command)
}

numbers = list(map(int, input().split()))
command = input().strip()

while command in commands:
    condition, transform = commands[command]
    numbers = [transform(x) if condition(x) else x for x in numbers]
    print(' '.join(map(str, numbers)))
    command = input().strip()
# Задание 16
import math

# Сначала объявляем класс Function
class Function:
    def __init__(self, name, left, op, right):
        self.name = name
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, x):
        left_val = self.left.evaluate(x) if isinstance(self.left, Function) else float(self.left)
        right_val = self.right.evaluate(x) if isinstance(self.right, Function) else float(self.right)

        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            return left_val / right_val
        else:
            raise ValueError(f"Unknown operator: {self.op}")

# Затем определяем предопределённые функции
x_function = Function('x', '0', '+', '0')
sqrt_fun = Function('sqrt_fun', '0', '+', '0')

# Переопределяем evaluate для них
def x_evaluate(self, x):
    return x

def sqrt_evaluate(self, x):
    return math.sqrt(x)

x_function.evaluate = x_evaluate.__get__(x_function, Function)
sqrt_fun.evaluate = sqrt_evaluate.__get__(sqrt_fun, Function)

# Создаём словарь функций
functions = {
    'x': x_function,
    'sqrt_fun': sqrt_fun
}

# Теперь читаем `n` и обрабатываем ввод
n = int(input())  # Теперь `n` определена перед использованием
for _ in range(n):
    parts = input().split()
    if not parts:
        continue

    if parts[0] == 'define':
        if len(parts) < 5:
            print("Error: 'define' requires 4 arguments (name, left, op, right)")
            continue

        name = parts[1]
        left = parts[2]
        op = parts[3]
        right = parts[4]

        # Проверяем left
        left_obj = None
        try:
            left_obj = float(left)
        except ValueError:
            if left in functions:
                left_obj = functions[left]
            else:
                print(f"Unknown function: {left}")
                continue

        # Проверяем right
        right_obj = None
        try:
            right_obj = float(right)
        except ValueError:
            if right in functions:
                right_obj = functions[right]
            else:
                print(f"Unknown function: {right}")
                continue

        functions[name] = Function(name, left_obj, op, right_obj)

    elif parts[0] == "calculate":
        if len(parts) < 2:
            print("Insufficient arguments for 'calculate'")
            continue

        func_name = parts[1]
        try:
            points = list(map(float, parts[2:]))
        except ValueError:
            print("Error: all arguments after function name must be numbers")
            continue

        if func_name not in functions:
            print(f"Unknown function: {func_name}")
            continue

        results = []
        for point in points:
            try:
                result = functions[func_name].evaluate(point)
                results.append(str(result))
            except Exception as e:
                results.append("error")
        print(' '.join(results))

    else:
        print(f"Unknown command: {parts[0]}")


# Задание 17
class Presentation:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration

    def overlaps(self, other):
        return not (self.end_time <= other.start_time or other.end_time <= self.start_time)

    def __str__(self):
        return f"Presentation('{self.topic}', {self.start_time}-{self.end_time})"


class Conference:
    def __init__(self):
        self.presentations = []

    def add_presentation(self, presentation):
        for existing in self.presentations:
            if existing.overlaps(presentation):
                print(f"Ошибка: доклад '{presentation.topic}' пересекается с '{existing.topic}'")
                return False
        self.presentations.append(presentation)
        self.presentations.sort(key=lambda p: p.start_time)
        print(f"Доклад '{presentation.topic}' успешно добавлен")
        return True

    def total_duration(self):
        return sum(p.duration for p in self.presentations)

    def max_break(self):
        if len(self.presentations) < 2:
            return 0
        breaks = [self.presentations[i + 1].start_time - self.presentations[i].end_time
                  for i in range(len(self.presentations) - 1)]
        return max(breaks) if breaks else 0

    def print_schedule(self):
        print("Расписание конференции:")
        for i, p in enumerate(self.presentations, 1):
            print(f"{i}. {p.topic} ({p.start_time}-{p.end_time})")
        print(f"Общая продолжительность: {self.total_duration()}")
        print(f"Самый длинный перерыв: {self.max_break()}")


# Пример использования
def run_conference_planner():
    conference = Conference()
    print("Добро пожаловать в планировщик конференций!")
    print("Доступные команды: add, schedule, exit")

    while True:
        command = input("> ").strip().lower()
        if command == 'exit':
            break
        elif command == 'add':
            topic = input("Введите тему доклада: ")
            start = float(input("Введите время начала: "))
            duration = float(input("Введите продолжительность: "))
            p = Presentation(topic, start, duration)
            conference.add_presentation(p)
        elif command == 'schedule':
            conference.print_schedule()
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    run_conference_planner()


# Задание 18
class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def write(self, content):
        self.content = content

    def read(self):
        return self.content


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

    def create_directory(self, path_components):
        if not path_components:
            return

        first = path_components[0]
        if first not in self.subdirectories:
            self.subdirectories[first] = Directory(first)

        if len(path_components) > 1:
            self.subdirectories[first].create_directory(path_components[1:])

    def get_directory(self, path_components):
        if not path_components:
            return self

        first = path_components[0]
        if first not in self.subdirectories:
            return None

        return self.subdirectories[first].get_directory(path_components[1:])

    def list_contents(self):
        dirs = list(self.subdirectories.keys())
        files = list(self.files.keys())
        return dirs + files

    def create_file(self, filename):
        if filename not in self.files:
            self.files[filename] = File(filename)

    def get_file(self, filename):
        return self.files.get(filename)


class FileSystem:
    def __init__(self):
        self.root = Directory("")

    def process_path(self, path):
        if not path:
            return []
        return path.split('/')

    def create_directory(self, path):
        components = self.process_path(path)
        self.root.create_directory(components)

    def list_directory(self, path):
        components = self.process_path(path)
        dir_obj = self.root.get_directory(components)
        if dir_obj is None:
            print(f"Директория {path} не существует")
            return []
        return dir_obj.list_contents()

    def write_file(self, filepath, content):
        components = self.process_path(filepath)
        if not components:
            print("Недопустимое имя файла")
            return

        filename = components[-1]
        dir_components = components[:-1]

        dir_obj = self.root.get_directory(dir_components)
        if dir_obj is None:
            print(f"Директория {'/'.join(dir_components)} не существует")
            return

        dir_obj.create_file(filename)
        dir_obj.get_file(filename).write(content)

    def read_file(self, filepath):
        components = self.process_path(filepath)
        if not components:
            print("Недопустимое имя файла")
            return ""

        filename = components[-1]
        dir_components = components[:-1]

        dir_obj = self.root.get_directory(dir_components)
        if dir_obj is None:
            print(f"Директория {'/'.join(dir_components)} не существует")
            return ""

        file_obj = dir_obj.get_file(filename)
        if file_obj is None:
            print(f"Файл {filepath} не существует")
            return ""

        return file_obj.read()


# Пример использования
def run_file_system():
    fs = FileSystem()
    print("Добро пожаловать в файловую систему!")
    print("Доступные команды: mkdir, ls, write, read, exit")

    while True:
        command = input("> ").strip().lower()
        if command == 'exit':
            break
        elif command == 'mkdir':
            path = input("Введите путь директории: ")
            fs.create_directory(path)
            print(f"Директория {path} создана")
        elif command == 'ls':
            path = input("Введите путь директории: ")
            contents = fs.list_directory(path)
            print("Содержимое:", ' '.join(contents))
        elif command == 'write':
            path = input("Введите путь файла: ")
            content = input("Введите содержимое: ")
            fs.write_file(path, content)
            print(f"Файл {path} записан")
        elif command == 'read':
            path = input("Введите путь файла: ")
            content = fs.read_file(path)
            print(f"Содержимое файла {path}: {content}")
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    run_file_system()
