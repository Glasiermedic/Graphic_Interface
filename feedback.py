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

        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!')
        ttk.Label(self.frame_header, text = ("We're glad you chose Glasierstudios for your photo needs."
        "Please tell us about your experience")

        self.frame_content = ttk.Frame(master)

        ttk.Label(self.frame_content, text = 'Name:')
        ttk.Label(self.frame_content, text = 'Email:')
        ttk.Label(self.frame_content, text = 'Comments:')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        ttk.Button(self.frame_content, text ='Submit')
        ttk.Button(self.frame_content, text = 'Clear')


        pass:

def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()