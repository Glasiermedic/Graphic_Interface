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
from tkinter import messagebox

class Feedback:
   

    def __init__ (self, master):
#creating a style for the look of our graphic interface
        master.title('Explore California Feedback')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold')) 

#creating the header portion of the GUI
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
#adding a logo to the header
        self.logo = PhotoImage(file = "C:/Users/sewmo/Desktop/LinkedInLearning/Ex_Files_Python_GUI_Dev_Tkinter/Ch08/tour_logo.gif")
#creating the text for the header  
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Thanks You").grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, padding = 10, text = ("We're glad you chose GLasier Studios. "
    "PLease tell us what you thought about the experience")).grid(row = 1, column = 1)
# creating the content portion of the GUI
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
    #creating the labels for the form entry fields    
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
    #creating the entry fields for form
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
    #creating the buttons for submitting and clearing the form   
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
    #Prints the inputs when the submit button is pushed
    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')

    #clears the form when the clear button is pushed
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
   