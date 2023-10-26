
if __name__ == '__main__':

    # dictionary of questions where key is the question and answer is the value.
    physics_quiz = {
        "What is the SI unit of electric current? ": "Ampere",
        "What is the fundamental particle that carries a negative electric charge?": "Electron",
        "What force opposes the relative motion of two surfaces in contact?": "Friction",
        "What property of an object determines its resistance to changes in motion?": "Mass",
        "What is the SI unit of luminous intensity?": "Candela"
    }

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