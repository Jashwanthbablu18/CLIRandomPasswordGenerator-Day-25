# Day-25Code.py

# Importing generate_password() from ExternalFile.py
from ExternalFile import generate_password

# main
def main():
    print("🔐 Random Password Generator")

    # This tries to take length and need for special characters from user as input
    try:
        # Takes password length as input
        length = int(input("Enter password length: "))

        # Asks user for is there any need to include special characters in password. and converts the input into lowercase.
        # If user enters other than 'y' or 'Y' it will be considered as "NO" means it won't include any special characters in password.
        special = input("Include special characters? (y/n): ").lower() == 'y'

        # passes the length and special charater to generate_password() function to generate the password. After generating displays the password.
        password = generate_password(length, special)
        print(f"✅ Generated Password: {password}")

    # If user enters any invalid input for password length then this msg will be displayed
    except ValueError:
        print("⚠️ Please enter a valid number for password length.")



# calling main() to starting execution of program
if __name__ == "__main__":
    main()
