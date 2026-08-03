commands_list = ["wink", "double blink","close your eyes", "jump", "reverse"]

def commands(binary_str):
    #Assuming len(binary_str) == 5
    answer = ""
    first_action = check(0, binary_str[4])
    second_action = check(1, binary_str[3])
    third_action = check(2, binary_str[2])
    fourth_action = check(3, binary_str[1])
    fifth_action = check(4, binary_str[0])

    answer = [first_action, second_action, third_action, fourth_action]
    answer = [action for action in answer if action is not None]
    if fifth_action == "reverse":
        answer.reverse()
    return answer

        
def check(index_commands, digit):
    if digit == "1":
        return commands_list[index_commands]
    else:
        return None