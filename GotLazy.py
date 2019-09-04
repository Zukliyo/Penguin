class Find_word():
  def __init__(self, string, integer=None): # integer=None not to get TypError  
    self.string = string
    self.integer = integer

  def find(self):
   # checking if you entered number
    try:
      self.integer = int(self.integer)
    except ValueError:
      return 'read second question carefully u dumb ass and enter the number'
    else:
     # trying to return nth word
      try:
        return self.string.split()[self.integer - 1]
      # if it is out of range then i will tell you how many words are in text
      except IndexError:
        self.string = self.string.split()
        return f"text contains only {len(self.string)} word"
  # staticmethod is mmm how to say... u r allowed not to pass self in this function :)) easy peasy
  @staticmethod
  # trying not to get int with base 10 error
  def inp():
    try:
      return int(input('Which word you need? ex: 1,2,3 etc.: '))
    except ValueError:
      return 'read second question carefully u dumb ass and enter the number'

# i call staticmethod from class and then function which is used to find word
start = Find_word(input('Enter text here:  '), Find_word.inp()).find()
#lessss goooooooo :/
print(start)
