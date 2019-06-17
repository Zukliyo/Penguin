# An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter
class Isogram:                                              
  def __init__(self, text_file):
    # initialisation of text file
    self.text_file = text_file                              

  def getter_setter(self):
    # trying to search file
    try:
      # opening file in mode read too see if this such file exists, if it exsists then this code below will work
      f = open(self.text_file, 'r')
      # need to read text in this file and also split them into list to read as words, not just as one sentence
      r = f.read().split()
      # for every word in this list of words i will count it's length and then i would compair it with the set of the same word. You sould know that in set there can't be duplicate letters 
      [ print(f"word {i} is an isogram") if len(i) is len(set(i)) else print(f"word {i} is not an isogram") for i in r]
      # finally close the file
      f.close()
      
       # otherwise it will tell you that file does not exists
    except:
      print('file does not exist')

# create object and give it text file which you want to be read
s = Isogram('text.txt')

# call the class function by name of class exmpl: class_name.Function_name()                                
s.getter_setter()                                           

