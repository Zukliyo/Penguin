# importing regex
import re
class Pangram():
  def __init__(self, text):
    # initialisation of text
    self.text = text
    
  def checker(self):
     # need to remove all WhiteSpaces so i replaced space ' ' with nothing '', i also lowercased sentence not to be case sensitive
    self.text= self.text.lower().replace(' ','')

    # in english there are 26 letters, so i checked if length set of letters in text were equal to 26,that's set so there can't be duplicate letters  
    if len(set(re.findall('[a-z]', self.text))) == 26:
      print('sentence is pangram')
    else:
      print('sentence is not pangram')
      
# sentence
s = Pangram('The quick brown fox jumps over the lazy dog')   
s.checker()


#Penguin