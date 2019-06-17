# importing whole tkinter library
from tkinter import * 

# creating function in which we are setting our action for my case it gives me the name and the last name 
def show():  
  # we are getting info from s1 which is input Button
  print(f'First Name: {s1.get()}\nLast Name: {s2.get()}')  

# creating function to save information   
def save():
  # opening file in write mode in which we want ot save the following info   
  f = open('data.txt', 'w')
  # writing to the file 
  f.write(f'First Name: {s1.get()}\nLast Name: {s2.get()}')
  # closing it
  f.close()  

master = Tk()
# text information and position
Label(master, text="First Name").grid(row=0)  
Label(master, text="Last Name").grid(row=1)   
# input Button
s1 = Entry(master) 
s2 = Entry(master)
# position,try yourself to understand
s1.grid(row=0, column=1) 
s2.grid(row=1, column=1)

# creating Button , giving him name and commant which we want him to do, and his tion
Button(master, text='Exit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4) 
Button(master, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Save', command=save).grid(row=3, column=2, sticky=W, pady=4)

mainloop()
