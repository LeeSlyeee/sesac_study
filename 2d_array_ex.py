
# 1. 중첩 리스트 (Nested Lists) - 가장 기본적인 방법
# 직접 값을 입력하여 생성
matrix_manual = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("1. 중첩 리스트 (수동):")
print(matrix_manual)
print()

# 2. 리스트 컴프리헨션 (List Comprehension) - 추천 방법
# 초기값(0)으로 3x4 배열 생성 (3행 4열)
rows = 3
cols = 4
matrix_comp = [[0 for j in range(cols)] for i in range(rows)]

print(f"2. 리스트 컴프리헨션 ({rows}x{cols}):")
for row in matrix_comp:
    print(row)
print()

# 주의: 아래와 같이 만들면 얕은 복사(Shallow Copy) 문제가 발생할 수 있음
# matrix_bad = [[0] * cols] * rows  # 이렇게 하면 한 행을 수정하면 다른 행도 같이 바뀜!

# 3. NumPy 사용 - 데이터 분석/과학용
import numpy as np

# 리스트를 numpy 배열로 변환
np_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 0으로 채운 배열 생성 (zeros)
np_zeros = np.zeros((3, 3))

print("3. NumPy 배열:")
print(np_array)
print("\nNumPy zeros (3x3):")
print(np_zeros)
