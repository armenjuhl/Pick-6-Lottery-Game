# Written by Armen Juhl 4/1/2020
import random


def main():
    val_flag = False
    while not val_flag:
        test_input = str(input('Pick 6 numbers between 1 and 99 separated by spaces'))

        try:
            split_list = list(test_input.split(' '))
            validated_list = list()
            for i in split_list:
                validated_list.append(int(i))
            if len(validated_list) == 6:
                val_flag = True
        except ValueError:
            print('You must enter 6 numbers between 1 and 99 to play')

    winning_nums = pick6()
    ticket = pick6()
    print('Winning Ticket ', winning_nums, '\nTicket is ', ticket)
    num_matches(winning_nums, ticket)


# Creates a list of 6 random integers
def pick6():
    set_list = list()
    for i in range(0, 6):
        set_list.append(create_random_number())
    return set_list


# Finds qualified matches. For pairs to match, ticket must match the winning numbers in the same index in the
# same sequence.
def num_matches(winning, ticket):
    true_matches = 0
    for idx1, tickVal in enumerate(ticket):
        for idx2, winVal in enumerate(winning):
            if tickVal == winVal and idx1 == idx2:
                true_matches += 1
    print('Number of matches = ', true_matches)
    return true_matches


def create_random_number():
    return random.randint(1, 99)
