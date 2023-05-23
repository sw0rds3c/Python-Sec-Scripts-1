import os   
import sys
import random
import string
import bcrypt   # pip install bcrypt

#PART1
# Creates a random passsword (string) of lower and uppercase letters, numbers, and special characters.
# Then adds this string to a text file.
# When the set number of passwords per file is met, open another file until the set file number count is met.
'''
numFiles = 4
numPasswords = 250
passwordLength = 12
cnt = 0    

try:
    
    print("Passwords:\n")

    for i in range(numFiles):
        filePath = 'PasswordList' + str(i+1) + '.txt'
        
        # open the file to write to
        with open(filePath,"a") as file:
        
            for i in range(numPasswords):
                
                password_characters = string.ascii_letters + string.digits + string.punctuation
                randomPassword = ''.join(random.choice(password_characters) for i in range(passwordLength))            
                
                file.write("\n" + randomPassword + "\n")
                
                cnt += 1
                
                print(cnt)
                
                print(randomPassword)            
        
        file.close() 
        
except Exception as err:
    print (str(err))
'''

#PART2
# Now we prompt the user for input to get the file path for the password list(s) to be hashed.
# For each password file, we want to pull all the entries from each file and hash them with bcrypt.
# Then we want to store those hashed entries in another text file for secure storage.

DIR = input("\nEnter File Path for password list processing -- (Text Files Only!): ")

for currentRoot, dirList, fileList in os.walk(DIR):
    
    for nextFile in fileList:
        
        fullPath = os.path.join(currentRoot, nextFile)
        absPath = os.path.abspath(fullPath) 
        ext = os.path.splitext(absPath)[1]
        
        print("\n" + fullPath + "\n" + absPath + "\n" + ext + "\n")
        
        if os.path.isfile(absPath) and ext.lower() == ".txt":
            
            targetFile = open(absPath, 'rt')
            
            fileContents = targetFile.readlines()
            
            converted_list = []
            
            for element in fileContents:
                
                converted_list.append(element.strip('\n'))
                converted_list = [x for x in converted_list if x != '']
                
                hashed_list = []
                
            for eachElement in converted_list:
                
                salt = bcrypt.gensalt(rounds=7)
                hash_object = bcrypt.hashpw(eachElement.encode(), salt)
                hex_dig = hash_object.decode()                            
                
                hashed_list.append(hex_dig)
        
                newFilePath = 'HashedPasswordList' + '.txt'
                
                newFile = open(newFilePath,"a")
                    
                newFile.write(hex_dig + "\n")
            
            print("\n Converted List: \n")
            print(converted_list)
            print("\n Salted & Hashed Passwords: \n")
            print(hashed_list)
