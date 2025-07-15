import math

def input_function(expr):
    """
    Создаёт функцию f(x) из введённого пользователем выражения.

    Поддерживаются функции из math, а также tg, ctg, cbrt, и константы e и pi.

    Args:
        expr (str): строка с выражением функции от x, например 'sin(x) - 0.5'

    Returns:
        function: функция от одного аргумента x, вычисляющая значение expr
    """

    # Дополнительные функции
    def tg(x):
        return math.tan(x)

    def ctg(x):
        if x == 0:
            raise ValueError("Котангенс не определён при x=0")
        return 1 / math.tan(x)

    def cbrt(x):
        if x >= 0:
            return x ** (1/3)
        else:
            return -((-x) ** (1/3))

    # Разрешённые имена для eval
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed_names.update({
        'tg': tg,
        'ctg': ctg,
        'cbrt': cbrt,
        'e': math.e,
        'pi': math.pi,
    })
    allowed_names['x'] = None  # сюда подставим значение x

    def f(x):
        allowed_names['x'] = x
        try:
            return eval(expr, {"__builtins__": None}, allowed_names)
        except Exception as e:
            raise ValueError(f"Ошибка вычисления функции в точке x={x}: {e}")

    return f


def dichotomy_method(f, a, b, epsilon, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("Функция должна менять знак на концах интервала (f(a)*f(b) < 0)")

    print(f"{'Итерация':>9} | {'a':>15} | {'b':>15} | {'c':>15} | {'f(c)':>20} | {'(b - a)/2':>15}")
    print("-" * 90)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        print(f"{i:9d} | {a:15.10f} | {b:15.10f} | {c:15.10f} | {fc:20.12e} | {(b - a)/2:15.12e}")

        if abs(fc) < epsilon or (b - a) / 2 < epsilon:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2


def main():
    print("Метод дихотомии для решения уравнения f(x) = 0.")
    print("Поддерживаются функции: sin, cos, tg, ctg, exp, log, cbrt, sqrt и константы e, pi.")
    expr = input("f(x) = ")
    expr = expr.replace('^', '**').lower()  # замена ^ на **, и приведение к нижнему регистру

    try:
        f = input_function(expr)
    except Exception as e:
        print(f"Ошибка при создании функции: {e}")
        return

    try:
        a = float(input("Введите левую границу интервала a: "))
        b = float(input("Введите правую границу интервала b: "))
        epsilon = float(input("Введите точность epsilon (>0): "))
        if epsilon <= 0:
            raise ValueError("Точность должна быть положительным числом.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return

    try:
        root = dichotomy_method(f, a, b, epsilon)
        print(f"\nПриближённое значение корня: {root:.10f}")
        print(f"Значение функции в корне: {f(root):.10e}")
    except Exception as e:
        print(f"Ошибка при вычислении корня: {e}")


if __name__ == "__main__":
    main()
