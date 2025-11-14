
CORRECT_USERNAME = "admin_user"   
CORRECT_PASSWORD = "S3cureP@ss!"    
MAX_ATTEMPTS = 3                    
def check_credentials(username: str, password: str) -> bool:
    """
    Return True if both username and password match the declared credentials.
    Comparison is exact and case-sensitive.
    """
    return username == CORRECT_USERNAME and password == CORRECT_PASSWORD
def login():
    """
    Run the interactive login simulation. User gets MAX_ATTEMPTS tries.
    """
    print("Welcome to the Login Simulation.")
    attempts_left = MAX_ATTEMPTS
    while attempts_left > 0:
        print(f"\nAttempts remaining: {attempts_left}")
        user_input = input("Username: ").strip()
        try:
            pass_input = getpass.getpass("Password: ")
        except Exception:
            pass_input = input("Password (input visible): ")
        if check_credentials(user_input, pass_input):
            print("\nLogin successful! Access granted.")
            print(f"Hello, {CORRECT_USERNAME}. You logged in at {time.asctime()}.")
            return True

        else:
            attempts_left -= 1
            print("Incorrect username or password.")
            time.sleep(0.6)
    print("\nToo many failed attempts. Your account is temporarily locked.")
    return False

if __name__ == "__main__":
    login()

