#오늘의집
def solution(products, purchased):
    character = []
    recommend = []
    for product in products:
        product = list(map(str, product.split()))
        product
        for purchase in purchased:
            if purchase == product[0]:
                character.extend(product[1:])
        if product[0] not in purchased:
            recommend.append(product)

    counts = []
    for char in character:
        num = character.count(char)
        if [char, num] not in counts:
            counts.append([char, num])
    counts.sort(key=lambda x: (-x[1], x[0]))
    recommend.sort(key=len)

    result = []
    for c in counts:
        temp = []
        if result == []:
            for r in recommend:
                if c[0] in r:
                    temp.append(r)
            result.append(temp)
        else:
            for re in result[0]:
                if c[0] in re:
                    temp.append(re)
            result.append(temp)
    print(result)
    result = sum(result, [])
    answer = []
    for r in result:
        num = result.count(r)
        if [r[0], num] not in answer:
            answer.append([r[0], num])
    answer.sort(key=lambda x: (-x[1], x[0]))
    print(answer)
    return answer[0][0]


    # c = counts[0][0]
    # result = []
    # for r in recommend:
    #     if c in r:
    #         result.append(r)
    # if len(result) == 1:
    #     return result[0][0]
    # c2 = counts[1][0]
    # result2 = []
    # for re in result:
    #     if c2 in re:
    #         result2.append(re)
    # if len(result2) == 1:
    #     return result2[0][0]
    
solution(["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"], ["towel", "mattress", "curtain"])
solution(["towel red long thin", "blanket red thick short", "curtain red long wide", "mattress thick", "hat red thin", "pillow red long", "muffler blue thick long"], ["blanket", "curtain", "hat", "muffler"])
pro = ["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"]
pur = ["towel", "mattress", "curtain"]
for i in pro:
    product = list(map(str, i.split()))
    if product[0] not in pur:
        print(product)

a = 'ch p'
s = 'prick p ch dd'
if a in s:
    print('a')

[['long', 2], ['blue', 1], ['cheap', 1], ['red', 1]]
[['sofa', 'red', 'long'], ['blanket', 'blue', 'long']]

a = sum([[['sofa', 'red', 'long'], ['blanket', 'blue', 'long']], [['blanket', 'blue', 'long']], [], []], [])
for i in a:
    print(i)
print(a.count(['blanket', 'blue', 'long']))