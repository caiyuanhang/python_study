import sys

int1 = 18
int2 = 20
int3 = 0
print('type of int1==', type(int1))
print('type of int2==', type(int2))
print('type of int3==', type(int3))

int4 = 1_000
int5 = 999_999_999
print('int4==', int4)
print('int5==', int5)

testNumMaxLen = 9 ** 9999
sys.set_int_max_str_digits(0)
print('testNumerLen==', testNumMaxLen)
