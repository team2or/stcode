# 2047. 신문 헤드라인
def news_headline():
    input_="The_headline_is_the_text_indicating_the_nature_of_the_article_below_it."
    return print(input_.upper())
news_headline()
print('\n')
#2050. 알파벳을 숫자로 변환
def alph1():
    input_='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet=[]
    result=''
    for i in input_:
        alphabet.append(i)
    for j in range(1,len(input_)+1):
        if j == 26:
            alphabet[j - 1] = str(j)
        else:
            alphabet[j - 1] = str(j) + ' '

        result += alphabet[j - 1]
    print(result)

def alph2():
    t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, len(t)+1):
        print(i, end=' ')

def alph_google():
    T =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(T)):
        print(ord(T[i]) - 64, end=" ")

print('')
alph_google()
print('')
alph1()
print('')
alph2()