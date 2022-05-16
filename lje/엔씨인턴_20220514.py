#문제1
s="aabbbccd" #2
s = "abebeaedeac" #3
def solution(s):
    dic = {}
    answer = 0
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for v in dic.values():
        if v%2 != 0:
            answer += 1
    return answer

#문제2
dates = ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15", "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"]
date_list = []
for date in dates:
    if '~' in date:
        pass
    else:
        if date not in date_list:
            date_list.append(date)


#문제3
data = ["1 GRAY 0", "2 MUSSEUK 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-GRAY 3", "6 SMALL-GRAY 3", "7 WHITE-MUSSEUK 4", "8 GRAY-MUSSEUK 4"]
data_graph = {}
for d in data:
    data_list = list(map(str,d.split()))
    if data_list[2] not in data_graph:
        data_graph[data_list[2]] = [data_list[:2]]
    else:
        data_graph[data_list[2]].append(data_list[:2])
    # if data_list[:2] not in data_graph:
    #     data_graph[data_list[:2]] = [data_list[2]]
    # else:
    #     data_graph[data_list[:2]].append(data_list[2])
print(data_graph)