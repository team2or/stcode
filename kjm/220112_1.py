# https://programmers.co.kr/learn/courses/30/lessons/72410
# Programmers 72410.

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'\.{2,}', '.', new_id)
    new_id = re.sub(r'^\.|\.$', '', new_id)
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
        
    return new_id