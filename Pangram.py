import re
class Pangram():
  def __init__(self, text):
    self.text = text   # initialisation of text
    
  def checker(self):
    self.text= self.text.lower().replace(' ','')    # need to remove all WhiteSpaces so i replaced space ' ' with nothing '', i also lowercased sentence not to be case sensitive
    if len(set(re.findall('[a-z]', self.text))) == 26:    # in english there are 26 letters, so i checked if length set of letters in text were equal to 26,that's set so there can't be duplicate letters  
      print('sentence is pangram')
    else:
      print('sentence is not pangram')

s = Pangram('The quick brown fox jumps over the lazy dog')   # sentence
s.checker()
