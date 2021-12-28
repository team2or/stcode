while True:
    headline = input("헤드라인을 입력해주세요 : ")
    # 내용이 없는 경우
    if bool(headline) == False:
        pass
    else:
        print(headline.upper())
        break