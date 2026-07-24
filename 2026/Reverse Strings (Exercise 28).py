def reverse(text):
    text_as_list = list(str(text))
    text_as_list.reverse()
    answer = ""
    for i in text_as_list:
        answer += i
    return answer