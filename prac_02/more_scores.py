from random import randint

def main():
    """Determine result and random scores and results"""
    score = int(input("Enter score: "))
    print(f"{score} is {determine_result(score)}")
    number_of_random_scores = randint(0,score)
    for i in range(number_of_random_scores):
        random_score = randint(0, 100)
        print(f"{random_score} is {determine_result(random_score)}")

def determine_result(score_number):
    """Determine result based on score."""
    if score_number < 0 or score_number > 100:
        return "Invalid"
    elif score_number >= 90:
        return "Excellent"
    elif score_number >= 50:
        return "Passable"
    else:
        return "Bad"

main()