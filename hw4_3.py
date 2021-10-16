def determinant(m):
    res = 0
    d1m = m[1][1] * m[2][2] * m[3][3] + m[2][1] * m[3][2] * m[1][3] + m[1][2] * m[2][3] * m[3][1]
    d1p = m[3][1] * m[2][2] * m[1][3] + m[3][2] * m[2][3] * m[1][1] + m[2][1] * m[1][2] * m[3][3]

    res += m[0][0] * (d1m - d1p)

    d2m = m[1][0] * m[2][2] * m[3][3] + m[2][0] * m[3][2] * m[1][3] + m[1][2] * m[2][3] * m[3][0]
    d2p = m[3][0] * m[2][2] * m[1][3] + m[3][2] * m[2][3] * m[1][0] + m[2][0] * m[1][2] * m[3][3]

    res -= m[0][1] * (d2m - d2p)

    d3m = m[1][0] * m[2][1] * m[3][3] + m[2][0] * m[3][1] * m[1][3] + m[1][1] * m[2][3] * m[3][0]
    d3p = m[3][0] * m[2][1] * m[1][3] + m[2][0] * m[1][1] * m[3][3] + m[3][1] * m[2][3] * m[1][0]

    res += m[0][2] * (d3m - d3p)

    d4m = m[1][0] * m[2][1] * m[3][2] + m[2][0] * m[3][1] * m[1][2] + m[1][1] * m[2][2] * m[3][0]
    d4p = m[3][0] * m[2][1] * m[1][2] + m[2][0] * m[1][1] * m[3][2] + m[3][1] * m[2][2] * m[1][0]

    res -= m[0][3] * (d4m - d4p)

    return res


m = eval(input())
print(determinant(m))