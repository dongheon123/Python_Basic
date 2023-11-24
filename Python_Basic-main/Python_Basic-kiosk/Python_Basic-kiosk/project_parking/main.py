# 주차타워 구현!
# 조건 : 1층 ~ 5층, 층별로 1대만 주차
#       차량번호: 숫자4자리
# 기능:
#   1) 차량입고
#   2) 차량출고
#   3) 차량조회
#   4) 프로그램 종료

# 설정
max_car = 5 # 최대 5대
car_cnt = 0 # 주차 대수 카운트
# 1. list comprehension
tower = ["" for i in range(max_car)]

# 2.for + list.append()

# for i in range(max_car):
#    tower.append("")
# 결과: ["","","","",""]
while True:
    print("="*50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("="*50)
    print("= 1.입고")
    print("= 2.출고")
    print("= 3.조회")
    print("= 4.종료")
    print("="*50)

    while True:
        select_num = int(input(">>번호: "))
        if 4 >= select_num > 0:
            break
        else:
            print("MSG: 올바른 번호를 입력하세요.")

    if select_num == 1:  # 입고
        # 입고1. 주차타워 공간 확인
        if car_cnt < max_car: # 입고
            car_num = input(">>입고 ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG: 입고 불가, 다른 곳으로 가..")
    elif select_num == 2:  # 출고
        # 1.차량 번호
        car_num = input(">>출고 ")
        # 2.주차 타워 check 차량번호
        if car_num in tower: # True -> 차량이 존재
            for i, car in enumerate(tower):
                if car == car_num: # 출고
                    tower[i] = "" # 타워에서 차량제거
                    car_cnt -= 1
                    break
        else: # False -> 차량 X
            print("MSG: 해당번호로 입고 된 차량이 없습니다.")

        #   2-1 X: 차 없음..
        #   2-2 출고(tower 값 = > 
        pass
    elif select_num == 3:  # 조회
        print("== 주차 타워 현황 ==")
        for i in range(len(tower)-1,-1,-1):
            print(f"> {i+1}층 {tower[i]}")
        pass
    elif select_num == 4:  # 종료
        print("MSG: 프로그램을 종료합니다.")
        exit()
    #가로 출력
    #print(1, end=" ")