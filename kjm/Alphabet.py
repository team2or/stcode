alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
r_text = ""

while True:
    try:
        text = input("알파벳을 입력해주세요 : ")
        # 200자가 넘는 경우
        if len(text) > 200:
            print("200자 이내로 입력해주세요.")
        # 내용이 없는 경우
        elif len(text) == 0:
            print("내용을 입력해주세요.")
        else:
            for i in text:
                try:
                    i.lower()
                except TypeError:
                    print(i)
                    continue
                else:
                    a = str(alphabet.index(i) + 1)
                    r_text = r_text + a + " "
            break
    # 내용이 알파벳이 아닌 경우
    except ValueError:
        pass

print(r_text)


    

