# 대칭인 원소들을 어떻게 찾을 수 있을까요? 서로 대칭이 되는 인덱스를 찾아야겠죠.

# 인덱스 0과 대칭되는 위치는 인덱스 len(numbers) - 1입니다.
# 인덱스 1과 대칭되는 위치는 인덱스 len(numbers) - 2입니다.
# 인덱스 2와 대칭되는 위치는 인덱스 len(numbers) - 3입니다.
# 대칭되는 두 인덱스를 left와 right라고 합시다.

# right = len(numbers) - left - 1로 관계를 표현할 수 있습니다.
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))

# 접근법 #2

# 위치 바꾸기를 쉽게 할 수 있는 방법도 있습니다. 피보나치 수열 과제에서 언급한 방법 기억나시나요?
# 강의에서 배우지는 않지만, 튜플(tuple)이라는 자료형을 이용해서 할당하는 겁니다. 튜플은 아래와 같이
# 표현합니다.

# korean_names = ('효선', '유신')
# english_names = 'hyoseon', 'yusin'

# print(type(korean_names))
# print(type(english_names))
# <class 'tuple'>
# <class 'tuple'>

# 위처럼 괄호를 통해 표현할 수도 있지만 , 로만 각 요소를 구분해도 튜플로 인식이 됩니다.

# 그럼 어떻게 위치를 쉽게 바꿀 수 있는지 코드를 보겠습니다.

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
