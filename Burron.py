from tkinter import *    # importing whole tkinter library

def show():    # creating function in which we are setting our action for my case it gives me the name and the last name 
   print(f'First Name: {s1.get()}\nLast Name: {s2.get()}')   # we are getting info from s1 which is input Button
   
def save():   # creating function to save information
  f = open('data.txt', 'w')   # opening file in write mode in which we want ot save the following info
  f.write(f'First Name: {s1.get()}\nLast Name: {s2.get()}')    # writing to the file 
  f.close()  # closing it

master = Tk()
Label(master, text="First Name").grid(row=0)   # text information and position
Label(master, text="Last Name").grid(row=1)   

s1 = Entry(master)    # input Button
s2 = Entry(master)

s1.grid(row=0, column=1)  # position,try yourself to understand
s2.grid(row=1, column=1)

Button(master, text='Exit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)  creating Button , giving him name and commant which we want him to do, and his tion
Button(master, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Save', command=save).grid(row=3, column=2, sticky=W, pady=4)

mainloop()
