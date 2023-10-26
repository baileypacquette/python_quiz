from game_dictionary import physics_quiz,computer_science_quiz
if __name__ == '__main__':

    quiz_choice = input('Which quiz would you like to attempt physics,computer science ')
    if quiz_choice == 'physics':
        allquestions = list(physics_quiz.keys())
    if quiz_choice == 'computer':
        allquestions = list(computer_science_quiz.keys())
    # ask the user the first question in the dictionary and store their answer.#
    score = 0
    for i in range(5):
        answer = input((allquestions[i]))

        if answer.title() == physics_quiz[allquestions[i]]:
            print('That is correct')
            score += 1
        else:
            print('That is incorrect')

    print(score)