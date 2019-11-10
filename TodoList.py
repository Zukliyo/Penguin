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
    return f'Data: {self.data.strftime("%d/%m/%Y %H:%M:%S")} \nTodo: {self.text}'


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
        line = line.split()  # creating list of all words in the file 

        if line[0] != 'Todo:':  # if the first word in the line is not todo, there should be 1), 2) or etc.
          del line[0]  # deleting first word on line, which is: 1)
          data_text = ' '.join(line)  # coverting this words to string again
          line_data.append(data_text)
        else:
          todo_text = ' '.join(line)
          line_todo.append(todo_text)
    
      d = dict(zip(line_data,line_todo))  # creating dict in which key is data and value is todo
      for k,v in d.items():  
        todo = Todo_from_file(f'{k}\n{v}')  # passing new todo with data to class todo_from_file
        manager.add_from_file(todo)  # calling Manager method to add todo in Database  
    
    # Menue
    while choice != 'q':
      print('\n\n>>>> To do list Menu <<<<')
      print('a) Add')
      print('e) Edit')
      print('d) Delete')
      print('s) Show all')
      print('q) Quit')

      choice = input('Action:  ').lower()
      
      # Creating todo
      if choice == 'a':
        text = input('To do:  ')
        todo = Todo(text)
        manager.add(todo)

      # Editing already existed todo
      elif choice == 'e':
        manager.show_all() # showing all todoes with their indexes
        entries = database.get_all()

        if len(entries) > 0:  # if entries is not empty

          try:
            index = int(input('enter index number to edit:  '))  # this is input for index, which u need for editing
          except IndexError:
            print('Invalid input')
          else:
            index = entries[index - 1]  # index - 1 because for now it starts with 1 
            text = input('To do:  ')
            new_todo = Todo(text)
            manager.update(index, new_todo)  # calling Manager class to update Database

      # Deleting todo
      elif choice == 'd':
        manager.show_all()  #showing all todoes to have choice
        entries = database.get_all()

        if len(entries) > 0:  # if it's not empty
          try:
            index = int(input('enter index number to edit:  '))  # index
            index = entries[index - 1]  # indexing should start from 0
          except IndexError:
            print('Invalid input')
          else:
            manager.delete(index)  # calling Manager method delete 

      # Show all
      elif choice == 's':
        manager.show_all()  # Manager method show_all
        
      # Quiting while loop
      elif choice == 'q':
        save = input('Wanna save to file? [y/n]:').lower()
      
      # Saving to file
        if save == 'y':
          f = open('Todo.txt', 'w')  # open file in write mode
          f.write(manager.to_file())  #calling Manager method to_file to save all todoes to file
          f.close()  # closing file
          
        else:
          pass
      else:
        pass


menu()  #lesss go


# >>>>>>>>>>>> Note <<<<<<<<<<<<<
# it won't work if you create todo file yourself, because simply just one space is important in this Todo.txt file 
# for example file looks like this:
#                                   1) Data: 10/11/2019 18:02:01 
#                                   Todo: note 1
#                                   2) Data: 10/11/2019 18:02:02 
#                                   Todo: note 2
#                                   3) Data: 10/11/2019 18:02:03 
#                                   Todo: note 3
#                                   4) Data: 10/11/2019 18:02:04 
#                                   Todo: note 4
#                                   5) Data: 10/11/2019 18:02:05 
#                                   Todo: note 5


#  >>>>>>>>>>>>>>>>>>>>> You need to create todoes with this programm instead <<<<<<<<<<<<<<<<<<<<<<<<<<<<







