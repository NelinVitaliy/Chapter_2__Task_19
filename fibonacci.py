#
# def fib(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# data = list(fib(10))
# print(data)


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


user_num = int(input("How many Fibonacci numbers you want generate?: "))

result = []
start = 1
for i in range(start, user_num + 1):
    result.append(fib(i))
print(result)




# def fibonacci(l):
#     if l == 0:
#         return 0
#     elif l in [1, 2] :
#         return 1
#     else:
#         return fibonacci(l-1) + fibonacci(l-2)

# print(fibonacci(8))




