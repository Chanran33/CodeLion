#커피 자판기 만들기
import time

#메뉴판
print("\t멋사 커피 자판기")

print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 초코라떼 2,300원")
print("\n========================================")

#알바생의 멘트
def notice(order,cream,temp,cups):
    order_ment = {1:'아메리카노',2:'카페라떼',3:"초코라떼"}
    cream_ment = {'Y':'휘핑추가','N':''}
    temp_ment = {'hot':'따뜻한','ice':'아이스'}

    print("\n========================================")
    print("주문하신 %s %s %s %d잔 나왔습니다." % (temp_ment[temp],order_ment[order],cream_ment[cream],cups))


#커피를 만들자
def makeCoffee(order, cream, temp, cups):
    temp_dic = {'hot': '''
         S    S 
      S    S    S''', 'ice': ''
    }
    cream_dic = {'Y': '''
           @@@
        @@@   @@
     @@@@      @@ 
    @            @  ''', 'N': ''}
    order_dic = {1:'''
    **************  
    **         ** ****
      **Coffee**  *** 
        ****** 
    ''', 2:'''
    **************  
    ***        *** 
    ****Coffee****  
      ****  ****
        ******  
    ''', 3:'''
    **************
  ***     *  *   *
  * *      **    * 
  * **   Choco  ** 
  ** **        ** 
      **********
    '''}
    return (temp_dic[temp]+cream_dic[cream]+order_dic[order])*cups

#손님^^ 거스름돈 받으시죠
def account(order, cream, cups):
    pricebord = [1800, 2700, 2300] 
    #휘핑 추가 500원
    cream_opt = {'Y':500, 'N':0}

    price = (pricebord[order-1]+cream_opt[cream])*cups
    print("총 금액은 %d 입니다." % price)
    
    #예외처리
    while(True):
        givememoney = int(input("돈을 투입해주세요 >>> "))
        if givememoney < price :
            print("투입된 금액이 총 금액보다 작습니다. 다시 투입 하십시오.")
        else:
            print("%d원 투입하셨습니다. 거스름 돈으로 %d원 드립니다." % (givememoney,givememoney-price))
            break

order = int(input("커피 종류를 선택하세요. 번호 입력 >>> "))

if order == 1:
    cream = 'N'
    temp = input("hot / ice를 선택하세요. (hot/ice) >>> ")
elif order == 2:
    cream = input("휘핑크림 추가해드릴까요? (Y/N) >>> ")
    temp = input("hot / ice를 선택하세요. (hot/ice) >>> ")
elif order == 3:
    cream = input("휘핑크림 추가해드릴까요? (Y/N) >>> ")
    temp = input("hot / ice를 선택하세요. (hot/ice) >>> ")

cups = int(input("몇 잔 드릴까요? >>> "))

account(order, cream, cups)
time.sleep(cups) #잔수 만큼 늦게 나옴
notice(order,cream,temp,cups)
print(makeCoffee(order, cream, temp ,cups))


