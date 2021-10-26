# ------------------------------------------------------------------------------
# Question 1
# The program will show whether the grades of two students are equal.
# ------------------------------------------------------------------------------

def main():
    # Collect both students' grade
    first = input('What is the first grade?')
    second = input('What is the second grade?')

    # Use "if else" to compare and give the answer of whether the grades of two
    # students are equal
    if first == second:
        print(first + ' and ' + second + ' are equal!')
    else:
        print(first + ' and ' + second + ' are NOT equal!')

main()