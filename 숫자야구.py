# 숫자 야구 게임을 시작합니다.
# 숫자를 입력해주세요 : 123
# 1볼 1스트라이크
# 숫자를 입력해주세요 : 145
# 1볼
# 숫자를 입력해주세요 : 671
# 2볼
# 숫자를 입력해주세요 : 216
# 1스트라이크
# 숫자를 입력해주세요 : 713
# 3스트라이크
# 3개의 숫자를 모두 맞히셨습니다! 게임 종료
# 게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.
# 1
# 숫자를 입력해주세요 : 123
# 1볼
# ...


import random


print("숫자 야구 게임을 시작합니다")
while(True):
    Number = []
    while len(Number) < 3:
        randomNumber = random.randint(1, 9)
        if randomNumber not in Number:
            Number.append(randomNumber)

    while(True):
        ballcounter=0
        strikecounter=0

        player_input=int(input("숫자를 입력해주세요"))

        if (not player_input in list(range(100,1000))) or '0' in str(player_input):
            raise Exception("IllegalArgumentException")

        player_input=[int(a)for a in str(player_input)]

        if (player_input[0] in Number):
            if player_input[0]==Number[0]:
                strikecounter+=1
            else:
                ballcounter+=1
        if (player_input[1] in Number):
            if player_input[1]==Number[1]:
                strikecounter+=1
            else:
                ballcounter+=1
        if (player_input[2] in Number):
            if player_input[2]==Number[2]:
                strikecounter+=1
            else:
                ballcounter+=1

        if(ballcounter+strikecounter==0):
            print("낫싱")
        else:
            print("{}볼 {}스트라이크".format(ballcounter,strikecounter))

        if strikecounter==3:
            print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
            break
    restart=int(input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요."))
    if restart==1:
        pass
    elif restart==2:
        break
    else:
        raise Exception("IllegalArgumentException")

    