# Simulates taking the exam; it computes the worst possible grade when
# using the protocol implemented in examCheatingCode

import exam_cheat_code
import itertools
import random


def sit_exams(exam_length = 20, message_length = 10):
    # generate all exams
    exams = []
    for exam in itertools.product([0, 1], repeat=exam_length):
        exams.append(exam)
    # randomize order, so next exam is not predictable
    random.shuffle(exams)

    worst_score = exam_length
    exams_to_check = len(exams)
    print("{} exams still to check".format(exams_to_check))
    for exam in exams:
        # encode copy of exam solutions in 10 bit
        copy = []
        copy[:] = exam
        code = exam_cheat_code.encode(copy)
        if len(code) != message_length or any(map(lambda b: b != 0 and b != 1, code)):
            raise Exception("Illegal code!")
        # compute answers to the exam from the 10 bit
        answers = exam_cheat_code.decode(code)
        if len(answers) != exam_length or any(map(lambda b: b != 0 and b != 1, answers)):
            raise Exception("Illegal decoded exam answers!")
        score = 0
        for i in range(exam_length):
            if answers[i] == exam[i]:
                score += 1
        if score < worst_score:
            worst_score = score
        # progress report
        if exams_to_check % 10000 == 0:
            print("{} exams still to check".format(exams_to_check))
        exams_to_check -= 1
    return worst_score

if __name__ == "__main__":
    my_worst_mark = sit_exams()
    # Print result
    print("The worst achieved mark is: " + str(my_worst_mark))
