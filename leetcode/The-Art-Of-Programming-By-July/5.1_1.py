"""
1、给定一个长度为N的整数数组，只允许用乘法，不能用除法，计算任意（N-1）个数的组合中乘积最大的一组，并写出算法的时间复杂度。
分析：我们可以把所有可能的（N-1）个数的组合找出来，分别计算它们的乘积，并比较大小。
由于总共有N个（N-1）个数的组合，总的时间复杂度为O（N2），显然这不是最好的解法。
"""