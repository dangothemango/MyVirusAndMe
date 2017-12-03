import hashlib

def main():
    # Collect user's password
    print ("Keys are not case sensitive")
    pass_input = raw_input('Enter level key: ')

    # Convert to all lowercase letters
    pass_input = pass_input.lower()

    # Hash given password
    hashed_input = hashlib.sha512(pass_input).hexdigest()
    #write_hash(hashed_input) #For collecting hashes of new levels

    # Display hashed password
    print hashed_input

    # Check if valid password is hashed_passwords file
    if check_hash(pass_input, hashed_input):
        print "Valid Key -- Unlocking Level..."
        raw_input()
    else:
        print "Invalid Key -- Try Again...\n\n"
        main()

# Write hash to file
def write_hash(hash):
    file = open("testFile.txt", "w")
    file.write(hash)
    file.close()

# Check if hash is in file
def check_hash(pass_input, hashed_input):
    with open("Hashed_Passwords", "r") as file:
        for line in file:
            line = line.strip('\n')
            info = line.split(":")
            print "Level: " + info[0]
            print "Hash: " + info[1]
            if hashed_input == info[1]:
                print "match found"
                #decrypt_files(pass_input, info[0])
                return True
    return False

# Decrypt the files for the valid hash
def decrypt_files(pass_input, level):
    pass
    # decrypt file name w/ password
    # save decrypted files to desktop?

main()
