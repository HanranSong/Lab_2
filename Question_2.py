# ------------------------------------------------------------------------------
# Question 2
# Find the highest grade among three grades.
# ------------------------------------------------------------------------------

def main():
    # Collect three different grades
    first = float(input('What is the first grade? '))
    second = float(input('What is the second grade? '))
    third = float(input('What is the third grade? '))

    # Compare three grades one by one to find the highest grade
    highest = first
    if second > highest:
        highest = second
    if third > highest:
        highest = third

    # Use build-in function to find the highest grade
    print('The highest grade is ' + str(highest))

main()