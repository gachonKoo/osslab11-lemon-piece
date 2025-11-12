balance = 10000  
transaction_history = []  

while True:
    print("\n=== ATM 서비스 ===")
    print("1. 입금 | 2. 출금 | 3. 잔액 확인 | 4. 내역 | 5. 종료")
    choice = input("선택: ")

    if choice == "1":
        deposit_amount = int(input("입금 금액: "))
        balance += deposit_amount
        transaction_history.append(("입금", deposit_amount))  
        print(f"→ 현재 잔액: {balance}원")

    elif choice == "2":
        withdrawal_amount = int(input("출금 금액: "))
        if withdrawal_amount > balance:
            print("잔액 부족")
        else:
            balance -= withdrawal_amount
            transaction_history.append(("출금", withdrawal_amount))  
            print(f"→ 현재 잔액: {balance}원")

    elif choice == "3":
        print(f"→ 현재 잔액: {balance}원")

    elif choice == "4":
        print("[거래 내역]")
        for transaction in transaction_history:
            print(f"{transaction[0]}: {transaction[1]}원")

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break  

    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")