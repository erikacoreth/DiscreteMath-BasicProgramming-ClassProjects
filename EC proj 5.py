from math import factorial

#Function to calculate the binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

#function to print pascal's triangle
def print_pascals_triangle(lines):
    max_width = 4 * lines - 3 #estimate the max width of the triangle for formatting
    for n in range(lines):
        row = []
        for k in range(n + 1):
            row.append(str(binomial_coefficient(n,k)))
        #join the row values into a string and center it
        row_str = ' '.join(row).center(max_width)
        print(row_str)

#main program to take user input
def main():
    while True:
        try:
            lines = int(input('Enter the number of lines for Pascals Triangle (4 to 8):'))
            if 4 <= lines <= 8:
                break
            else:
                print('Please enter a number between 4 and 8,')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    print_pascals_triangle(lines)

if __name__ == '__main__':
    main()
    
