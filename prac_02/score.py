SCORE_MIN = 0
SCORE_MID = 50
SCORE_HIGH = 90
SCORE_MAX = 100


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    if SCORE_MIN < score < SCORE_MID:
        level = "bad"
    elif score < SCORE_HIGH:
        level = "pass"
    elif score < SCORE_MAX:
        level = "excellent"
    else:
        level = "Invalid"
    return level


main()
