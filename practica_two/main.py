def input_function(expr):
    """
    Создаёт функцию f(x) из введённого пользователем выражения.

    Аргументы:
        expr (str): строка с выражением функции от x, например 'sin(x) - 0.5'

    Возвращает:
        function: функция от одного аргумента x, вычисляющая выражение expr
    """
    import math
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed_names['x'] = None  # добавим ключ 'x'

    def f(x):
        allowed_names['x'] = x
        return eval(expr, {"__builtins__": None}, allowed_names)

    return f


def dichotomy_method(f, a, b, epsilon, max_iter=100):
    """
    Метод дихотомии для поиска корня уравнения f(x)=0 на [a, b].

    Аргументы:
        f (function): функция одной переменной
        a (float): левая граница интервала
        b (float): правая граница интервала
        epsilon (float): требуемая точность
        max_iter (int): максимальное число итераций

    Возвращает:
        float: приближённое значение корня
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала (f(a)*f(b) < 0).")

    print(f"{'Итерация':>9} | {'a':>12} | {'b':>12} | {'c':>12} | {'f(c)':>14} | {'(b - a) / 2':>14}")
    print("-" * 75)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        print(f"{i:9d} | {a:12.8f} | {b:12.8f} | {c:12.8f} | {fc:14.8e} | {(b - a)/2:14.8e}")

        if abs(fc) < epsilon or (b - a) / 2 < epsilon:
            return c  # корень найден с нужной точностью

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    # Если корень не найден за max_iter итераций — возвращаем последнее приближение
    return (a + b) / 2


def main():
    print("Метод дихотомии для решения уравнения f(x) = 0.")
    print("Введите функцию f(x). Можно использовать функции из math, например: sin(x), cos(x), exp(x), log(x).")
    expr = input("f(x) = ")

    try:
        f = input_function(expr)
    except Exception as e:
        print("Ошибка при создании функции:", e)
        return

    try:
        a = float(input("Введите левую границу интервала a: "))
        b = float(input("Введите правую границу интервала b: "))
        epsilon = float(input("Введите точность epsilon (>0): "))
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")
        return

    if epsilon <= 0:
        print("Ошибка: точность epsilon должна быть положительным числом.")
        return

    try:
        root = dichotomy_method(f, a, b, epsilon)
        print(f"\nПриближённое значение корня: {root:.10f}")
        print(f"Значение функции в корне: {f(root):.10e}")
    except Exception as e:
        print("Ошибка при вычислении корня:", e)


if __name__ == "__main__":
    main()
