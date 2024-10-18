import math

def get_valid_input(prompt, min_val, max_val):
    #Helper function to get valid input within a given range
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f'Please enter a value between {min_val} and {max_val}.')

        except ValueError:
            print(f'Invalid Input. Please enter a number.')
            

def main():
    #step 1- get number of subsets (j)
    j = get_valid_input(f'Enter the number of subsets (j) (between 3 and 8): ', 3, 8)

    #step 2- get size of each subset (mi)
    subsets = []
    for i in range(j):
        mi = get_valid_input(f'Enter the size of subset (m) {i+1} (between 1 and 5):', 1, 5)
        subsets.append(mi)

        #step 3- compute the total number of elements (n)
    n = sum(subsets)

        #step 4: get the total number of elements to arrange (k)
    k = get_valid_input(f'Enter the number of elements to arrange (k) (must be smaller than {n}):', 1, n-1)

        #step 5- calculate the number of arrangements
    def arrangements(k, n, subsets):
        # calculate n! / (n-k)!
        numerator = math.factorial(n)
        denominator = math.factorial(n-k)

        #Multiply by the factorial of each subset size
        for mi in subsets:
            denominator *= math.factorial(mi)

        #the result is the number of arrangements
        return numerator // denominator
    

    #step 6- compute and print the result
    num_arrangements = arrangements(k, n, subsets)
    print(f'Given your inputs, the number of arrangments is {num_arrangements}')

if __name__ == '__main__':
    main()
#makes sure it computes what I wrote at the def main() above this

