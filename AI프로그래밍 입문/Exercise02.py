names = []
scores = []

while True:
    print("\n=== 학생 성적 관리 프로그램 ===")
    print("1. 학생 추가 | 2. 전체 목록 보기 | 3. 평균/최고/최저 점수 보기 | 4. 특정 학생 점수 검색 | 5. 종료")
    choice = input("선택: ")

    if choice == "1":
        name = input("학생 이름을 입력하세요: ")
        if name in names:
            print("이미 등록된 학생입니다.")
        else:
            score = int(input(f"{name}의 점수를 입력하세요: "))
            names.append(name)  
            scores.append(score)  
            print(f"{name} 학생이 추가되었습니다.")

    elif choice == "2":
        if names:  
            print("\n전체 학생 목록:")
            for i in range(len(names)):
                print(f"{names[i]}: {scores[i]}점")
        else:
            print("등록된 학생이 없습니다.")

    elif choice == "3":
        if names:  
            avg_score = sum(scores) / len(scores)
            max_score = max(scores)
            min_score = min(scores)
            print(f"평균: {avg_score:.2f}점")
            print(f"최고점: {max_score}점")
            print(f"최저점: {min_score}점")
        else:
            print("등록된 학생이 없습니다.")

    elif choice == "4":
        search_name = input("검색할 학생 이름을 입력하세요: ")
        if search_name in names:
            index = names.index(search_name)
            print(f"{search_name}의 점수는 {scores[index]}점입니다.")
        else:
            print("해당 학생이 없습니다.")

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break  

    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")