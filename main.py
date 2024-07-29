import random
import Questions

def get_question(q, options, qnum):
    random.shuffle(options)
    option_labels = ['a', 'b', 'c', 'd']
    print(f'{qnum + 1}) {q}\n')
    for idx, option in enumerate(options):
        print(f'{option_labels[idx]}) {option}')
    return opt, option_labels

score = 0
qnum = 0
questions = Questions.shuffled_questions

def display_question(option_labels, correct_ans):
    user_input = input('Choose the correct option (a/b/c/d): ')
    if user_input in option_labels:
        suhff_index = option_labels.index(user_input)
        optio = opt[suhff_index]
        if optio == correct_ans:
            print("You're Right")
            score_l = 1
        else:
            print("You're Wrong")
            score_l = 0
    else:
        print("Invalid Choice, Select b/w a, b, c or d")
        display_question(option_labels, correct_ans)
        score_l = 0
    return score_l


for q, opt in questions.items():
    correct_ans = opt[0]
    shuff_options, option_labels = get_question(q, opt, qnum)
    score += display_question(option_labels, correct_ans)
    qnum +=1
    if qnum == 5:
        break

print(f'Your total score is {score}/{qnum} ({score/qnum * 100})')
