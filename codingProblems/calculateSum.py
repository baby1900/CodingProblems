from sympy.abc import i
from sympy import Sum, factorial, ln


iFactorial = factorial(i)
iPlusOneFactorial = factorial(i + 1)
i2 = 2 * i
i2_1 = 2 * i + 1
for x in range(2, 101, 2):
    tempNum = x * 0.01
    n2lnx = -2 * ln(tempNum)
    x4_2 = 2 * (tempNum ** 4)
    infSum1 = Sum((1 / (iFactorial * iFactorial)) * (n2lnx ** i2), (i, 0, 1000))
    infSum2 = Sum((1 / (iFactorial * iPlusOneFactorial)) * (n2lnx ** i2_1), (i, 0, 1000))
    totalSum = x4_2 * (infSum1.doit() + infSum2.doit())
    print(totalSum)