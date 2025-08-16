import sys; input = sys.stdin.readline


# 입력 처리
n = int(input())
arr = [*map(int, input().split())]

# 목표 정렬 상태
sorted_arr = sorted(arr)

# --- 연산 1 (합이 홀수) 경우 확인 ---

# 원본 배열에서 짝수와 홀수를 순서대로 추출
evens_in_original = [num for num in arr if num % 2 == 0]
odds_in_original = [num for num in arr if num % 2 != 0]

# 추출된 짝수 리스트와 홀수 리스트가 이미 정렬된 상태인지 확인
if evens_in_original == sorted(evens_in_original) and \
    odds_in_original == sorted(odds_in_original):
    print("So Lucky")
else:
    print("Unlucky")

# --- 연산 2 (합이 짝수) 경우 확인 ---

is_possible_even_swap = True
# 원본 배열과 정렬된 배열의 각 위치의 패리티(짝/홀)가 동일한지 확인
for i in range(n):
    if arr[i] % 2 != sorted_arr[i] % 2:
        is_possible_even_swap = False
        break

if is_possible_even_swap:
    print("So Lucky")
else:
    print("Unlucky")