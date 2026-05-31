"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def main():
    """ Get score and display result."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = float(input("Enter score: "))
    print(determine_result(score))

def determine_result(score):
    """Determine result based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()