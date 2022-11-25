#!python

menu = "1. 입력 \n2. 출력 \n3. 검색 \n4. 종료"   # 메인메뉴 문장을 menu 변수에 저장
info = []                                       # 정보가 담길 list 선언

while True:  # 무한반복
    print(menu)  # 메인메뉴 문장 출력
    number = input("메뉴를 선택하세요.:")   # number 변수에 데이터 입력

    if number == '1':                            # 메인메뉴에서 누른 번호가 1 일 경우
        conti = 'y'                             # 밑의 while 문을 작동 시키기 위한 초기값
        while conti == 'y':                    # conti 변수가 y 일 경우
            value = {}                          # 제품에 대한 정보가 담길 딕셔너리 선언
            value['name'] = input("제품명:")   # name 에 제품명 입력
            value['quantity'] = input("수량:")  # quantity 에 수량 입력
            value['date'] = input("생산일(예:1990-01-01):")  # date 에 일자 입력
            conti = input("계속 입력하시겠습니까?(y/n)")  # conti 의 값 입력
            info.append(value)  # info 에 value 값 추가

            if conti == 'n':                   # conti 가 n 일 경우
                break

    if number == '2':                            # 메인메뉴에서 누른 번호가 2 일 경우
        print("-----------------------------------------------")
        print("     제품명          수량          생산일     ")
        print("-----------------------------------------------")  # 메뉴 출력
        i = 0                                   # 아래에서 쓰일 반복문을 위한 변수 선언
        while i < len(info):                   # i가 info의 요소 개수보다 작을 때까지
            # info 의 i 번째 요소의 딕셔너리의 name 에 대한 value 값 출력
            print('     ' + info[i]['name'], end='           ')
            # info 의 i 번째 요소의 딕셔너리의 quantity 에 대한 value 값 출력
            print(info[i]['quantity'], end='          ')
            # info 의 i 번째 요소의 딕셔너리의 date 에 대한 value 값 출력
            print(info[i]['date'])
            i = i + 1                           # 반복문 진행 시 마지막에 i가 1씩 증가

    if number == '3':                            # 메인메뉴에서 누른 번호가 3 일 경우
        find = input("검색할 제품명을 입력 하세요 :")  # 검색할 제품명 입력
        names = []                              # 제품명 검색을 위한 리스트 선언
        i = 0                                   # 아래에서 쓰일 반복문을 위한 변수 선언
        while i < len(info):                   # i가 info의 요소 개수보다 작을 때까지
            names.append(info[i]['name'])      # names 리스트에 제품명들을 모두 입력
            if find in names:                  # names 리스트에 찾는 제품명이 있을 경우, 제품에 대한 정보 출력
                print("-----------------------------------------------")
                print("     제품명          수량          생산일     ")
                print("-----------------------------------------------")
                print('     ' + info[i]['name'], end='           ')
                print(info[i]['quantity'], end='          ')
                print(info[i]['date'])
                break
            i = i + 1

    if number == '4':                            # 메인메뉴에서 누른 번호가 4일 경우
        really = input("프로그램을 종료 하시겠습니까(y/n)?")
        if really == 'y':                        # y 를 입력할 경우 프로그램 종료, n일 경우 메인메뉴
            break
