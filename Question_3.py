# ------------------------------------------------------------------------------
# Question 3
# Analyze the given grade and sort it based on its value
# ------------------------------------------------------------------------------

def main():
    # Collect the grade
    grade = float(input('Input the grade: '))

    # Use "if elif else" to find which category the grade best fit and show the
    # result
    if 3.3 <= grade <= 4:
        print('The grade is Excellent!')
    elif 2.3 <= grade < 3.3:
        print('The grade is Good!')
    elif 1.3 <= grade < 2.3:
        print('The grade is Satisfactory!')
    elif 1 <= grade < 1.3:
        print('The grade is Poor!')
    elif 0 <= grade < 1:
        print('The grade is Failure!')
    else:
        print('The grade is invalid!')


main()
