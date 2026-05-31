"""
Get a password and check whether it is valid
"""

MINIMUM_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print_astricks(password)

def print_astricks(password: str):
    """Print an astrick for each character in password."""
    print("*" * len(password))

def get_password() -> str:
    """Get password from user and check if it meets minimum character length"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password is too short!")
        password = input("Enter password: ")
    return password

main()
