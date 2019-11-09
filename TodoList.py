import datetime
# Class which i use as database
class Database:
  entries = []  # the actual database
  def add(self, todo):  # method that is adding some todo lists into entries 
    self.entries.append(todo)

  def add_from_file(self, todo):  # adding todo list from file
    self.entries.append(todo)

  def remove(self, ind):  # removing todo from entries with indexes
    index = self.entries.index(ind)
    del self.entries[index]

  def update(self, old_todo, new_todo):  # editing todo with indexes
    index = self.entries.index(old_todo)
    self.entries[index] = new_todo

  def get_all(self):  # this method is used to show all todo lists
    return self.entries


# Todo class in case there is file called Todo.txt that contains some todo  
class Todo_from_file:
  def __init__(self, text):
    self.text = text

  def __str__(self):  # returning todo, in this case date and todo text
    return self.text
        

# Just todo class
class Todo:
  def __init__(self,text):
    self.text = text
    self.data = datetime.datetime.now()  # generating datetime for this moment(when it would be used)

  def __str__(self): # this method is used to return todo in a nice way 
    return f'Data: {self.data.strftime("%d/%m/%Y %H:%M")} \nTodo: {self.text}'


# I used Manager class for managing processes(adding to datebase from class Todo or Todo from file, also for remove, update and show todoes)
class Manager:
  def __init__(self,datebase):  # inicializing datebase class to see it's methods and use them(i will do that later, like this: Manager(Datebase))
    self.datebase = datebase

  def add(self, todo):  # method which calls another method from class Database
    self.datebase.add(todo)  # calling method add from class Database 

  def add_from_file(self, todo):  # i used another add method for adding in datebase the already existed todoes which is in Todo.txt(if it existes of course) 
    self.datebase.add_from_file(todo)  # calling add_from_file method from class Datebase

  def show_all(self):  # this method is used to show all todoes 
    entries = self.datebase.get_all()  # calling ge_all method from class Datebase
    
    # And because my database is list i will use for loop to catch one todo at a time
    for item in entries:
      print('\n' + '>' * 15 +  '   ' + str(entries.index(item) + 1) + '   ' + 15 * '<')  # printing index for todo
      print(item)  # todo
      print('_' * 42)  # separator for another todo

  def to_file(self):  # method is used to generate text, leter for writing it in Todo.txt file   
    text = ''
    for index,item in enumerate(self.datebase.get_all()):
      text += str(index + 1) + ') ' + ''.join(str(item)) + '\n'  # example: 1) Data: 02/06/2019 17:32 
    return text                                                              # Todo: sleep well :)

  def update(self, old_todo, new_todo):  # editing todo
    entries = self.datebase.update(old_todo, new_todo)   # updating old todo with new one

  def delete(self, index): # remove
    entries = self.datebase.remove(index)  # calling class Database method to remove todo by indexing


# function making the whole program work
def menu(): 
    choice = None
    database = Database()
    manager = Manager(database)  # now class Manager can see and call class Database's methods
    
    try:
      r = open('Todo.txt', 'r')  # trying to find and read Todo.txt file
      print('    File found\n>>> Get started <<<')
    except:
      print(' No Todo list yet \n>>> Get started <<<')
    else:
      line_todo = []
      line_data = []

      for line in r:
        line = line.split()  # spliting words in line

        if line[0] != 'Todo:':  # if first wor in line is not todo, there should be 1), 2) and etc.
          del line[0]  # deleting 1)
          data_text = ' '.join(line)
          line_data.append(data_text)    
        else:
          todo_text = ' '.join(line)
          line_todo.append(todo_text)
    
      d = dict(zip(line_data,line_todo))
      for k,v in d.items():
        todo = Todo_from_file(f'{k}\n{v}')
        manager.add_from_file(todo)
      
    while choice != 'q':
      print('\n\n>>>> To do list Menu <<<<')
      print('a) Add')
      print('e) Edit')
      print('d) Delete')
      print('s) Show all')
      print('q) Quit')

      choice = input('Action:  ').lower()

      if choice == 'a':
        text = input('To do:  ')
        todo = Todo(text)
        manager.add(todo)


      elif choice == 'e':
        manager.show_all()      
        entries = database.get_all()

        if len(entries) > 0:

          try:
            index = int(input('enter index number to edit:  '))
          except IndexError:
            print('Invalid input')
          else:
            index = entries[index - 1]
            text = input('To do:  ')
            new_todo = Todo(text)
            manager.update(index, new_todo)


      elif choice == 'd':
        manager.show_all()
        entries = database.get_all()

        if len(entries) > 0:
          try:
            index = int(input('enter index number to edit:  '))
            index = entries[index - 1]
          except IndexError:
            print('Invalid input')
          else:
            manager.delete(index)


      elif choice == 's':
        manager.show_all()

      elif choice == 'q':
        save = input('Wanna save to file? [y/n]:').lower()

        if save == 'y':
          f = open('Todo.txt', 'w')
          f.write(manager.to_file())
          f.close()
          
        else:
          pass

      else:
        pass


menu()


