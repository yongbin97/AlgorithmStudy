import sys


def calculate(expression, alpha_value):
    val_list = []

    for exp in expression:
        if exp.isalpha():
            val_list.append(alpha_value[exp])

        else:
            b = val_list.pop()
            a = val_list.pop()

            if exp == "*":
                val_list.append(a * b)
            elif exp == "/":
                val_list.append(a / b)
            elif exp == "+":
                val_list.append(a + b)
            elif exp == "-":
                val_list.append(a - b)

    return val_list[0]


N = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
alpha_value = {}
for i in range(N):
    alpha_value[chr(i + 65)] = int(sys.stdin.readline())
print(f"{calculate(expression, alpha_value):.2f}")

