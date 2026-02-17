def solution(typedText):
    upper_count = 0
    lower_count = 0
    for ch in typedText:
        if ch.isupper():
            upper_count +=1
        elif ch.islower():
            lower_count +=1
    return upper_count - lower_count

