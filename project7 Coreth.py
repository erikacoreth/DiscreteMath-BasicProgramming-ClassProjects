import math

#function to calculate combinations (n choose k)
def combinations(n, k):
    return math.comb(n, k)

#function to calculate probabilities
def calculate_probabilities(n, k):
    #total combinations of selecting k numbers from n numbers
    total_combinations = combinations(n, k)

    #probability of winning big (hitting all k numbers)
    prob_win_big = 1 / total_combinations

    #probability of winning little (hitting k-1 numbers)
    prob_win_little = (combinations(k, k-1) * combinations(n-k, 1)) / total_combinations

    return prob_win_big, prob_win_little

#main program
def lottery_game():
    n = int(input('Enter the total number of possible numbers (n):'))
    k = int(input('Enter the number of numbers to bet on (k):'))

    #ensure valid input
    if k > n:
        print('Error: k cannot be greater than n')
        return

    #calculate the probabilities
    prob_win_big, prob_win_little = calculate_probabilities(n, k)

    #display the results
    print(f'\nThe probability of winning big (hitting all {k} numbers): {prob_win_big:.10f}')
    print(f'The probability of winning little (hitting {k-1} numbers): {prob_win_little:.10f}')

#run the program
lottery_game()
