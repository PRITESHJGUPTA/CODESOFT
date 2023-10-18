#python program to create a random password based on user defined length

#importing the random module for creating random password
import random
#using string to genrate a password
import string

def generate_password(length):
    # Defining the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("ENTER THE PASSWORD LENGTH::"))
        if password_length <= 0:
            print("INVALID PASSWORD LENGTH!!.")
        else:
            generated_password = generate_password(password_length)
            print("YOUR GENERATED PASSWORD IS:", generated_password)
    except ValueError:
        print("INVALID PASSWORD LENGTH!! PLEASE ENTER A VALID POSIVIVE INTEGER!!")
