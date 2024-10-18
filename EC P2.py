def convert_to_decimal(number, base):
    decimal = 0
    #starts at 0, so the number 245, the 2 is in the 2's spot, not 3.
    power = len(number) - 1
    for digit in number:
        #returns True if all the characters are digits, otherwise False
        if digit.isdigit():
            value = int(digit)
        else:
            #ord used to convert a single Unicode character into its integer representation
            #The upper() method returns a string where all characters are in upper case
            value = ord(digit.upper()) - ord('A') + 10
        decimal += value * (base ** power)
        power -= 1
    return decimal

n = input("Enter a number between 0 and 9 or A and F: ")
base = int(input("Enter the base (between 2 and 16): "))

decimal_representation = convert_to_decimal(n, base)
binary_representation = bin(decimal_representation)[2:]

print(f"{n} in base {base} is: {decimal_representation} in base 10 and {binary_representation} in base 2.")
