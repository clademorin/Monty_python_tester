import random

count = 2000000

def python_tester(count, switch_flag):
    result = 0

    for i in range(count):
        doors = [0,0,0]
        doors[random.randint(0,2)] = 1
        player_choice = doors.pop(random.randint(0,2))
        if doors[0] == 1:
            host_choice = 1
        else:
            host_choice = 0
        if switch_flag == False and player_choice == 1:
                result += 1
        if switch_flag == True and player_choice == 0:
                result += 1
    return result

print(f"Testing the scheme {str(count)} times, changing doors when asked\n")
switch = python_tester(count, True)
print(f"Testing the scheme {str(count)} times, NOT changing doors when asked\n")
no_switch = python_tester(count, False)

print(f"Changing doors, we guessed right {switch} times on {count}, for a precision of {str((switch/count)*100)}")
print(f"Not Changing doors, we guessed right {no_switch} times on {count}, for a precision of {str((no_switch/count)*100)}")