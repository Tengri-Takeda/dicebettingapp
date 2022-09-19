import random

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num_dice):

    #return integer of 1 and 6

    roll_results = []
    for _ in range (1):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    resultz = roll_results[-1]
    return resultz
def checking_if_correct_number_was_chosen(roll_results):
    if num_dice == roll_results:
        final_result = "Correct"
        return final_result
    else:
        final_result = "Wrong"
        return final_result


num_dice_input = input("What number do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
roll_results = roll_dice(num_dice)
print(roll_results)
final_answer=checking_if_correct_number_was_chosen(roll_results)
print(final_answer)




