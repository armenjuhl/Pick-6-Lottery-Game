import random


class Pick6Game:
    def __init__(self):
        self.earnings = 0
        self.expenses = 0
        self.roi = 0


game = Pick6Game()


def main():
    play_pick_6_x_times(100000)


def play_pick_6_x_times(num):
    for i in range(0, num):
        play_pick_6(game)
    print('Earnings', game.earnings, '\nExpenses ', game.expenses, '\nROI ', str(game.roi) + '%')


def play_pick_6(session_obj):
    session_obj.expenses -= 2

    winning_nums = pick6()
    user_ticket = pick6()

    # Calculate results
    matches = num_matches(winning_nums, user_ticket)
    game_earnings = calculate_earnings(matches)
    session_obj.earnings += game_earnings
    session_obj.roi = roi(session_obj.earnings, session_obj.expenses)
    # print('\nNew game\nWinning numbers: ', winning_nums, '\nYour numbers: ', user_ticket)
    # print('Number of matches: ', matches)
    # print('You earned: $', game_earnings)
    # print('You spent: $', session_obj.expenses)
    # print('Your ROI is ', session_obj.roi)
    return


def pick6():
    set_list = list()
    for i in range(0, 6):
        set_list.append(create_random_number())
    return set_list


def num_matches(winning, ticket):
    true_matches = 0
    for idx, val in enumerate(ticket):
        if val == winning[idx]:
            true_matches += 1
        return true_matches


def create_random_number():
    return random.randint(1, 99)


def calculate_earnings(user_matches):
    game_earnings = 0
    if user_matches == 1:
        game_earnings = 4
    elif user_matches == 2:
        game_earnings = 7
    elif user_matches == 3:
        game_earnings = 100
    elif user_matches == 4:
        game_earnings = 50000
    elif user_matches == 5:
        game_earnings = 1000000
    elif user_matches == 6:
        game_earnings = 25000000
    return game_earnings


def roi(user_earnings, user_expenses):
    user_expenses = user_expenses * -1
    return (user_earnings - user_expenses) / user_expenses * 100


if __name__ == '__main__':
    main()
