

import random
import string

def genrate_password(length):
    num = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(num) for _ in range(length))
    return password

def main():
    print("Password genrate opration is start.")
    try :
        length = int(input("enter the desired length of the password: "))
        if length <= 0 :
            print("Password length should be a positive integer. ")
            return
        password = genrate_password(length)
        print(f"Password Genrate: {password}")
    except ValueError :
        print("Invalid Input. Please enter the postive integer for the password length.")

if __name__ == '__main__' :
    main()