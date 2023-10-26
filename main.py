from game_dictionary import physics_quiz,computer_science_quiz
if __name__ == '__main__':

    # dictionary of questions where key is the question and answer is the value.

    # ask the user the first question in the dictionary and store their answer.
    score = 0
    allquestions = list(physics_quiz.keys())

    for i in range(5):
        answer = input((allquestions[i]))

        if answer.title() == physics_quiz[allquestions[i]]:
            print('That is correct')
            score += 1
        else:
            print('That is incorrect')

    print(score)