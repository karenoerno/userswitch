import os
import subprocess
import ctypes
from getpass import getpass

def is_user_admin():
    """Checks if the current user has administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def switch_user(username, password):
    """Switches to the specified user account."""
    try:
        command = f'runas /user:{username} "cmd"'
        subprocess.run(command, input=password.encode(), shell=True)
    except Exception as e:
        print(f"Failed to switch user: {e}")

def list_users():
    """Lists all user accounts on the system."""
    try:
        users = subprocess.check_output('net user', shell=True)
        print(users.decode())
    except Exception as e:
        print(f"Failed to list users: {e}")

def main():
    if not is_user_admin():
        print("This program requires administrator privileges. Please run as administrator.")
        return

    print("Welcome to UserSwitch.")
    print("Choose an option:")
    print("1. List all user accounts")
    print("2. Switch user account")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        list_users()
    elif choice == '2':
        username = input("Enter the username to switch to: ")
        password = getpass("Enter the password for the user: ")
        switch_user(username, password)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()