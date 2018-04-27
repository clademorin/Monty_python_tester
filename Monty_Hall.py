import random
import time

count = 2000000

def python_tester(count, switch_flag):
    result = 0
    percent = 1
    step = count/10

    for i in range(count):
        if i%step == 0:
            print(f"Simulation at {percent}0%")
            percent +=1
        #create a list for the doors and randomly select one as the winner
        doors = [0,0,0]
        doors[random.randint(0,2)] = 1
        #remove from the list the one the player selected
        player_choice = doors.pop(random.randint(0,2))
        #the host show the other one (note how the host_choice isn't called ever again)
        if doors[0] == 1:
            host_choice = 1
        else:
            host_choice = 0
        #if the player doesn't switch door and it has chosen the right one, he win
        if switch_flag == False and player_choice == 1:
                result += 1
        #if the player switch door and he has chosen the wrong one, he win
        if switch_flag == True and player_choice == 0:
                result += 1
        #We generate a random number of random values, just to mess with the seed
        for i in range(random.randint(0,3)):
            random.randint(0,3)
    print ("\n")
    return result

print(f"Testing the scheme {str(count)} times, changing doors when asked\n")
start_time=time.time()
switch = python_tester(count, True)
time_switch = time.time() - start_time

print(f"Testing the scheme {str(count)} times, NOT changing doors when asked\n")
start_time=time.time()
no_switch = python_tester(count, False)
time_no_switch = time.time() - start_time

print(f"Changing doors, we guessed right {switch} times on {count}, for a precision of {str((switch/count)*100)}; the simulation took {time_switch} seconds")
print(f"Not Changing doors, we guessed right {no_switch} times on {count}, for a precision of {str((no_switch/count)*100)}; the simulation took {time_no_switch} seconds")