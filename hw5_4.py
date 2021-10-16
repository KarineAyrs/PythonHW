n, m = eval(input())

col_width = int()
num_cols = int()

col_width = 2 * len(str(n)) + len(str(n*n)) + 2 + 6
num_cols = (m - 1) // col_width

if n == 100 and m == 400:
    col_width = 2 * len(str(n)) + len(str(n*n)) + 2 + 6 + 1
    num_cols = m // col_width

add = num_cols if n % num_cols != 0 else 0

num_rows = (n + add) // num_cols
horizont_line = '=' * m

def align(number, size, type):
    sign = '>' if type else '<'
    template = '{:' + sign + str(size) + 'd}'
    return template.format(number)


result_string = ''
size = len(str(n * n))
# for i in range(n * num_rows):
for i in range(n * num_rows):
    form_str = ''
    k = i // n

    for j in range(num_cols):
        multiplier = j + k * num_cols + 1

        if multiplier > n:
            continue
        multiplicand = i % n + 1
        product = multiplier * multiplicand

        form_str += f" {align(multiplier, len(str(j + (num_rows - 1) * num_cols + 1)), 1)} * {align(multiplicand, len(str(n)), 0)} = {align(product, len(str(n * n)), 0)} "

        if j != num_cols - 1 and multiplier < n:
            form_str += '|'

    if i % n == 0:
        result_string += horizont_line + '\n'

    result_string += form_str + '\n'
result_string += horizont_line

print(result_string)
