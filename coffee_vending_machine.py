class CoffeeVendingMachine:
    def __init__(self):
        self.recipe = {
            "americano": [("bean", 25), ("hot_water", 8)],
            "cafelatte": [("bean", 25), ("hot_milk", 8)],
            "matchalatte": [("matcha", 25), ("hot_milk", 8)],
            "espresso": [("bean", 30)]
        } # 음료별 레시피 딕셔너리

        self.ingredient = {
            "bean": 50,
            "matcha": 50,
            "hot_water": 100,
            "hot_milk": 100,
            "ice": 90
        } # 재료별 초기 재고 딕셔너리

        self.price = {
            "americano": 2000,
            "cafelatte": 2500,
            "matchalatte": 3000,
            "espresso": 1500
        } # 음료별 가격 딕셔너리

        self.question = """
1. 아메리카노
2. 카페라테
3. 말차라테
4. 에스프레소
원하시는 음료의 번호를 골라주세요 : """ # 음료 선택 질문 문자열

    def select_beverage(self): # 음료 선택 함수
        try:
            selected_number = int(input(f"{self.question}")) # input 값은 str으로 받음.
        except ValueError:
             print("잘못된 번호입니다. 다시 선택해주세요.")
             return self.select_beverage()

        selected_beverage = "" # 빈 문자열 생성
        
        if selected_number == 1: # 아메리카노 선택 시
            selected_beverage = "americano" # 선택한 음료를 문자열로 저장
        elif selected_number == 2: # 카페라테 선택 시
            selected_beverage = "cafelatte" # 선택한 음료를 문자열로 저장
        elif selected_number == 3: # 말차라테 선택 시
            selected_beverage = "matchalatte" # 선택한 음료를 문자열로 저장
        elif selected_number == 4: # 에스프레소 선택 시 
            selected_beverage = "espresso" # 선택한 음료를 문자열로 저장
        
        else: # 잘못된 번호 입력 시
            print("잘못된 번호입니다. 다시 선택해주세요.") # 잘못된 번호 메시지 출력
            return self.select_beverage() # 재귀 호출로 다시 음료 선택 함수 실행
            
        # return 값은 str으로 받음.
        return selected_beverage # 선택한 음료 문자열 반환
        

    def print_price(self): # 가격 출력 함수
        pick_beverage = self.select_beverage() # 음료 선택 함수 호출
        print(f"{pick_beverage}의 가격은 {self.price[pick_beverage]}원 입니다.") # 선택한 음료의 가격 출력   


    def pay_money(self, pick_beverage): # 결제 함수
        
        try: # 숫자가 아닌 값이 입력되면 여기서 ValueError가 발생합니다.
            paid_amount = int(input(f"{pick_beverage}의 가격은 {self.price[pick_beverage]}원 입니다. 금액을 투입해주세요: "))      
        except ValueError: # 숫자가 아닌 값이 들어왔을 때 실행됨
            print("[오류] 숫자만 입력 가능합니다. 다시 시도해주세요.")
            return self.pay_money(pick_beverage) # 재귀 호출로 다시 결제 함수 실행

        # --- 정상적으로 숫자가 입력되었을 때 실행되는 로직 ---
        if paid_amount < self.price[pick_beverage]: # 결제 금액이 음료 가격보다 적을 시
            print("금액이 부족합니다. 다시 투입해주세요.") 
            return self.pay_money(pick_beverage) # 재귀 호출
        else: # 결제 금액이 음료 가격보다 많거나 같을 시
            change = paid_amount - self.price[pick_beverage] # 잔돈 계산
            print(f"결제가 완료되었습니다.\n잔돈은 {change}원 입니다.") 
            return pick_beverage # 선택한 음료 문자열 반환
        

    def make_beverage(self): # 음료 제조 함수
        pick_beverage = self.select_beverage() # 음료 선택 함수 호출
       
        # 얼음 선택 로직
        is_ice = False
        while True:
            try:
                temp_choice = int(input("1. 따뜻하게  2. 차갑게 (얼음 추가)\n번호를 선택해주세요: "))
                if temp_choice == 1: # 따뜻한 음료 선택 시   
                    is_ice = False
                    break # 따뜻한 음료 선택 완료 후 루프 탈출
                elif temp_choice == 2: # 차가운 음료 선택 시
                    is_ice = True
                    break # 얼음 선택 완료 후 루프 탈출
                else:
                    print("잘못된 번호입니다. 다시 선택해주세요.")
            except ValueError:
                print("숫자를 입력해주세요.")

        for ingredient_name, required_amount in self.recipe[pick_beverage]: # 선택한 음료의 레시피 순회
            if self.ingredient[ingredient_name] < required_amount: # 재고가 부족할 시
                print(f"{ingredient_name} 재고가 부족합니다. 다른 음료를 선택해주세요.") # 재고 부족 메시지 출력
                return self.make_beverage() # 재귀 호출로 다시 음료 제조 함수 실행

        if is_ice:
            if self.ingredient["ice"] < 30: # 얼음 30g 소모 가정
                print("얼음 재고가 부족합니다. 다른 음료를 선택해주세요.")
                return self.make_beverage()

        self.pay_money(pick_beverage) # 결제 함수 호출
       
        for ingredient_name, required_amount in self.recipe[pick_beverage]: # 선택한 음료의 레시피 순회
            self.ingredient[ingredient_name] -= required_amount # 재고에서 사용한 재료만큼 차감
        
        if is_ice:
            self.ingredient["ice"] -= 30
            print(f"아이스 {pick_beverage}가 완성되었습니다. 맛있게 드세요!") # 음료 완성 메시지 출력
        else:
            print(f"따뜻한 {pick_beverage}가 완성되었습니다. 맛있게 드세요!") # 음료 완성 메시지 출력


    def check_ingredient(self): # 재고 확인 함수
        print("현재 재고 현황:") # 재고 현황 메시지 출력
        for ingredient_name, amount in self.ingredient.items(): # 재고 딕셔너리 순회
            print(f"{ingredient_name}: {amount}g") # 재고 출력


    def continue_or_not(self): # 계속 진행 여부 함수
        user_input = input("계속 진행하시겠습니까? (y/n): ") # 사용자 입력 받기
        if user_input.lower() == 'y': # 'y' 입력 시
            return True # 계속 진행
        elif user_input.lower() == 'n': # 'n' 입력 시
            print("이용해주셔서 감사합니다. 안녕히 가세요!") 
            return False # 종료
        else: # 잘못된 입력 시
            print("잘못된 입력입니다. 다시 입력해주세요.") 
            return self.continue_or_not() # 재귀 호출로 다시 계속 진행 여부 함수 실행


    def run(self): # 커피 자판기 실행 함수
        while True: # 무한 루프
            self.make_beverage() # 음료 제조 함수 호출
            self.check_ingredient() # 재고 확인 함수 호출
            
            if not self.continue_or_not(): # 계속 진행 여부가 False일 시
                break # 루프 종료
            
            
if __name__ == "__main__":
    machine = CoffeeVendingMachine()
    machine.run()
