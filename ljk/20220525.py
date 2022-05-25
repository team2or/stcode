#20220519
import re
def spliting(f_name):
    f_name = f_name.lower()
    head = re.match('[\D]+', f_name)
    num = re.search('[0-9]+', f_name)
    file = [head[0], int(num[0]), f_name[num.end():]]
    return file

def solution(files):
    new_files = []
    for i, file in enumerate(files):
        s_file = spliting(file)
        s_file.append(i)
        new_files.append(s_file)
    new_files.sort(key=lambda x: (x[0], x[1], x[-1]))

    answer = list(map(lambda x: files[x[-1]], new_files))
    return answer
print(solution(["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]))