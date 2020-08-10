""" Tasks to complete
 - Header Frame 
    label logo
    label header
    label message

 - content frame
     label name
     label eamil
     label comments
     entry name
     entry email
     entry comments
     submit button
     clear button
Calling on CSV file 
writing to CSV
Storing to CSV file 

"""

""" Tasks completed  """ 



from tkinter import *
from tkinter import ttk 

class Feedback:
 

    def __init__ (self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = "C:/Users/sewmo/Desktop/LinkedInLearning/Ex_Files_Python_GUI_Dev_Tkinter/Ch08/tour_logo.gif")
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Thanks You").grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, padding = 10, text = ("We're glad you chose GLasier Studios. "
    "PLease tell us what you thought about the experience")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24).grid(row = 1, column = 0, padx = 5)
        self.entry_email = ttk.Entry(self.frame_content, width = 24).grid(row = 1, column = 1, padx = 5)
        self.text_comments = Text(self.frame_content, width = 40, height = 10, ).grid(row = 3, column = 0, columnspan=2, padx = 5)

        ttk.Button(self.frame_content, text ='Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Name: {}'.format(self.text_comments.get(1.0,'end')))
        self.clear()
        


    def clear(self):
        self.entry_name.delete(0,'end')
        self.entry_email.delete(0,'end')
        self.text_comments.delete(1.0,'end')

def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": 
    main()
   