# 문제1) 사용자가 입력한 단수를 출력하는 코드 (구구단)
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i} = {dan*i}")


# 문제2) 2단부터 9단까지 출력(중첩 for문)
# for i
#     for j
#         for k
for i in range(2, 10):             # 큰 반복
    for j in range(1, 10):         # 작은 반복
        print(f"{i}x{j} = {i*j}")  # 작은 반복 먼저 끝나면 큰 반복


# 문제 3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a의 길이 => len(a)
total = 0
for num in a:
    total = total + num  # total += num  # 총합 계산
result = total/len(a)

# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2))   # 평균값

# 문제4) 숙제@@ list b에서 최솟값 찾기
b = [22, 1, 4, 7, 98]
num_min = b[0] # 최소값 담을 공간
for x in a: # 5번 반복
    if x < num_min:
        num_min = x

print(num_min)  # 1 출력

# 문제5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]
num_max = c[0]
for x in c:
    if x < num_min:
        num_min = x

for x in c:
    if x > num_max:
        num_max = x
print(num_min) # 1 출력
print(num_max) # 8 출력


print("="*100)
# 사용자가 입력한 값 1,2,3 통과
# 아닌 경우 다시 입력하도록

# 문제6번)
count = 0 # 틀린 횟수
while True:
    if count >=3:
        print("프로그램을 사용할 수 없습니다.")
        break

    num = int(input("값: "))
    if num in [1, 2, 3]:
        print(f"{num}을 입력하셨습니다.")
        break

    else:
        print("1,2,3의값만 입력해주세요")
        count += 1
# 문제7) 1부터 100까지 총합을 출력하는 코드
# - for문으로 작성
total = 0
for num in range(1,101):
    total += num
print(f"총합(for): {total}")

# - while문으로 작성
num = 0
total = 0
while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"총합(while): {total}")




