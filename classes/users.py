class Users(object):
    def __init__(self, name, email, password, confirm):
        self.name = name
        self.email = email
        self.password = password
        self.confirm = confirm

    def register(self, name, email, password, confirm):
        #validate that the name given is not a number or contain other characters and symbols
        #validate the email address
        #validate that the password and confirm passwords match
        #check if the user exists in the users dict
        #return message if the user exists
        #Add the user to the users dict
        #take the details for email and passwrd and log the user in
        #redirect to the home page
        pass
    
    def login(self, email, password):
        #validate the email and password
        #check users dict if the email exists
        #if email does not exist, return a message
        #if email exists, check if the given password mathces saved password for the email
        #if id does not match, return wrong password error
        # if password matches, login the user and create a session for the user
        pass
    
    def logout(self):
        #logout the user by destroying the session
        pass