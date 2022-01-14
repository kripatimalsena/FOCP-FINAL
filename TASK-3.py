import random 

def valid_email(email):#function to validate email
    if email.count("@")!=1:
        return False
    
    if len(email.split("@")[0])<2:
        return False

    if email.split("@")[1]!="pop.ac.uk":
        return False
    
    return True

def greeting(name):#fuction to greet the user
     print(f"Thanks, {name}, for using PopChat. See you again soon!")
    
connection_error=[0,0,0,0,0,0,0,0,0,1]
Operator=random.choice(["Helen", "Mary", "West", "Sandy", "Fiona", "John"])#shows the operator in random format
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email=input("Please enter your Poppleton email address: ")

if valid_email(email):#checks whether the email is valid or not
    name = email.split("@")[0].capitalize()
    print(f"Hi, {name}! Thank you, and Welcome to PopChat! \nMy name is {Operator}, and it will be my pleasure to help you.")

    while True:
        if random.choice(connection_error) == 1:
            print("*** NETWORK ERROR ***")
            greeting(name)
            break
        question=input("-->")
        if any(char in question.lower() for char in ["bye","exit","help","goodbye","end"]):#if we use this words in the statement the progrma will close
            greeting(name)
            break    
        elif("library" in question.lower()):
            print("The library is closed today.")
        elif("wifi" in question.lower()):
            print("WiFi is excellent across the campus.")
        elif "deadline" in question.lower():
            print( "Your deadline has been extended by two working days.")
        elif "book" in question.lower():
            print( "You can access the book from the library")
        elif "cafe" in question.lower():
            print( "The cafe is right next to the library")
        elif "classes" in question.lower():
            print( "You have no classes today")
        else:
            print(random.choice(["hmm","I didn't understand","I see","sorry", "Oh, yes, I see.", "Is it?"]))#if the statement is out of the given words it will show these statement 
            
else:
    print("This email is not valid")#show this when the email is not according to the given format