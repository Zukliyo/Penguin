class Isogram:    #  An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter
  def __init__(self, text_file):
    self.text_file = text_file     #  initialisation of text file

  def getter_setter(self):
    try:    #   trying to search file
      f = open(self.text_file, 'r')        # opening file in mode read too see if this such file exists, if it exsists then this code below will work
      r = f.read().split()      #  need to read text in this file and also split them into list to read as words, not just as one sentence
      [ print(f"word {i} is an isogram") if len(i) is len(set(i)) else print(f"word {i} is not an isogram") for i in r]   #  for every word in this list of words i will count it's length and then i would compair it with the set of the same word. You sould know that in set there can't be duplicate letters 
      f.close()        #  finally close the file 
    except:        # otherwise it will tell you that file does not exists
      print('file does not exist')
      
s = Isogram('text.txt')         #  create object and give it text file which you want to be read
s.getter_setter()         #  call the class function by name of this class_name.Function_name()

