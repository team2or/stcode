
def solution(dirs):

    step = set()

    point = [0,0]

    for dir in dirs:
        point_dir = None
        reverse_point_dir = None

        if dir == "U" and point[1] +1 <= 5:
            point_dir= (point[0], point[1], dir)
            point[1] += 1
            reverse_point_dir = (point[0], point[1], 'D')

        elif dir =='D' and point[1]-1 >= -5:
            point_dir = (point[0], point[1], dir)
            point[1] -= 1
            reverse_point_dir = (point[0], point[1], 'U')

        elif dir =='R' and point[0]+1 <= 5:
            point_dir = (point[0], point[1], dir)
            point[0] += 1
            reverse_point_dir = (point[0], point[1], 'L')

        elif dir =='L' and point[0]-1 >= -5:
            point_dir = (point[0], point[1], dir)
            point[0] -= 1
            reverse_point_dir = (point[0], point[1], 'R')

        step.add(point_dir)
        step.add(reverse_point_dir)
    return len(step)//2
