# https://programmers.co.kr/learn/courses/30/lessons/12926
# Programmers 12926.

def solution(s, n):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    result = ''
    for i in s:
        if i not in alphabet:
            if i.lower() not in alphabet:
                result += i
            elif i.lower() in alphabet:
                if i.lower() == "z":
                    result += alphabet[-1+n].upper()
                else:
                    index = alphabet.index(i.lower())
                    result += alphabet[index+n].upper()                
        else:
            if i == "z":
                result += alphabet[-1+n]
            else:
                index = alphabet.index(i)
                result += alphabet[index+n]
    return result
