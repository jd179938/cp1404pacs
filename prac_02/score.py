"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint

def main():
    """ Get score and display result."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = float(input("Enter score: "))
    print(f"User score {score} is {determine_result(score)}")
    random_score = randint(1,100)
    print(f"Random: {random_score} = {determine_result(random_score)}")

def determine_result(score):
    """Determine result based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()