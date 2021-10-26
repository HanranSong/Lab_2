# ------------------------------------------------------------------------------
# Lab 2 Conditional Statements Lab
# Tell students which exercise they should do next based on their two quizzes'
# marks.
# ------------------------------------------------------------------------------

def main():
    # Collect two quizzes' mark
    quiz_1 = float(input('Enter marks for quiz 1 >'))
    quiz_2 = float(input('Enter marks for quiz 2 >'))

    # Using conditional statement to find out which category does the student
    # best fit in and show them
    if quiz_1 >= 80 and quiz_2 >= 80:
        print('Level 3')
    elif quiz_1 >= 50 and quiz_2 >= 50:
        print('Level 2')
    elif quiz_1 < 50 and quiz_2 < 50:
        print('Level 1')
    elif quiz_1 < quiz_2:
        print('Redo quiz1')
    elif quiz_2 < quiz_1:
        print('Redo quiz2')


main()
