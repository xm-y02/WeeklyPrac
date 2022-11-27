SCORE_MIN = 0
SCORE_MID = 50
SCORE_HIGH = 90
SCORE_MAX = 100

MENU = "(G)et a valid score\n(P)rint result \n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    score = float(input("Please enter your score first: "))
    get_valid_score(score)
    choice = input("<<< Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Please enter your score: "))
            get_valid_score(score)
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid.")
        print(MENU)
        choice = input("<<< Your choice: ").upper()
    else:
        print("Farewell.")


def get_valid_score(score):
    while score <= SCORE_MIN or score >= SCORE_MAX:
        print("Invalid.")
        score = float(input("Please enter your score: "))
    return score


def determine_score(score):
    if SCORE_MIN < score < SCORE_MID:
        level = "Bad"
    elif score < SCORE_HIGH:
        level = "Pass"
    elif score <= SCORE_MAX:
        level = "Excellent"
    else:
        level = "Invalid"
    return level


def show_stars(score):
    print('*' * int(score))


main()
