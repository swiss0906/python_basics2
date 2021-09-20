numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.
for i in range(len(numbers)):
    print(i, numbers[i])
# for index, value in enumerate(numbers, start=1):
#     print(index, value)

# a = [38, 21, 53, 62, 19]
# for index, value in enumerate(a):
# ...     print(index, value)
# ...
# 0 38
# 1 21
# 2 53
# 3 62
# 4 19

# 앞의 코드는 인덱스를 0부터 출력하는데 1부터 출력하고 싶을 수도 있습니다.
# 다음과 같이 그냥 index + 1을 출력하면 되겠죠?

# >>> for index, value in enumerate(a):
# ...     print(index + 1, value)
# ...
# 1 38
# 2 21
# 3 53
# 4 62
# 5 19

# 하지만 좀 더 파이썬 다운 방법이 있습니다. 다음과 같이 enumerate에 start를 지정해주면 됩니다.

# >>> for index, value in enumerate(a, start=1):
# ...     print(index, value)
# ...
# 1 38
# 2 21
# 3 53
# 4 62
# 5 19
