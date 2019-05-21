class Isogram:
  def __init__(self, text_file):
    self.text_file = text_file

  def getter_setter(self):
    try:
      f = open(self.text_file, 'r')
      r = f.read().split()
      [ print(f"word {i} is an isogram") if len(i) is len(set(i)) else print(f"word {i} is not an isogram") for i in r]
      f.close()
    except:
      print('file does not exist')
      
s = Isogram('text.txt')
s.getter_setter()

