def solution(s):
    text_l = s.split(" ")
    result = ""
    for i in text_l:
        word = ""
        for j in range(len(i)):
            if j%2 == 0:
                word += i[j].upper()
            elif j%2 == 1:
                word += i[j].lower()
        if i == text_l[-1]:
            result += word
        else:
            result += word + " "
    return result

