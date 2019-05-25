import re

class P:
  def __init__(self, password):
    self.password = password

  def validate(self): 
      # checking if password length is more than 6, then code bellow will work
      if len(self.password) > 6:
        # checking if there is symbols in string which is the password
        if re.search('[^A-Za-z0-9]', self.password):
          print('Password contains symbols that are not allowed')
        # checkin that the password has numbers in it
        elif re.search('[0-9]',self.password) is None:
          print('Password must contain at least one number')
        # checking for capital letters in password
        elif re.search('[A-Z]',self.password) is None:
          print('Password must contain at least one capital letter')
       # anything else is allowed :)
        else:
          print('Your password is allowed')
      # if length of the password is less than 6, other checks won't work
      else:
        print('Password must be at least 6 characters long')
        
        
s = P(input('Enter password:  '))
s.validate()
