"""
# TODO: Fix this!

"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")


# Fixed version
SCORE_MIN = 0
SCORE_MID = 50
SCORE_HIGH = 90
SCORE_MAX = 100

score = float(input("Enter score: "))
if SCORE_MIN < score < SCORE_MID:
    level = "Bad"
elif score < SCORE_HIGH:
    level = "Pass"
elif score < SCORE_MAX:
    level = "Excellent"
else:
    level = "Invalid score"

print(level)