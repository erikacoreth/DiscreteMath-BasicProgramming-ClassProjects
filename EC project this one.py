def geometric_progression():
    # Ask the user for the scale factor and common ratio
    a = float(input("Enter the scale factor (a): "))
    r = float(input("Enter the common ratio (r): "))

    # Check if the GP converges to a sum
    if abs(r) < 1:
        # GP converges to a sum
        sum_infinite = a / (1 - r)
        print(f"The GP converges with infinite elements to {sum_infinite}")
    else:
        # GP does not converge to a sum
        n = int(input("Enter the number of elements (n): "))
        sum_finite = a * (1 - r**n) / (1 - r)
        print(f"The GP does not converge to a finite number with infinite elements.")
        print(f"The GP sum with {n} elements is equal to {sum_finite}")

    # Print the first 3 elements of the GP
    first_element = a
    second_element = a * r
    third_element = a * r**2
    print(f"The first elements are {first_element}, {second_element}, {third_element}")

# Run the function
geometric_progression()
