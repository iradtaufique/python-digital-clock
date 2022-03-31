from tkinter import *
import time

root = Tk()

root.title('My Digital clock')  # setting project title
root.geometry('800x400')  # setting the project window size


"""function to display current time and day"""
def myTime():
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%A')
    timeLabel.config(text=current_time)
    dayLabel.config(text=current_day)

    timeLabel.after(1000, myTime)  # this line will be repeated every second to display seconds dynamic


timeLabel = Label(root, text='', font=('Ariel', 72), fg='white', bg='black')
dayLabel = Label(root, text='', font=('Ariel', 26))

timeLabel.pack()  # showing the result to project window
dayLabel.pack()  # showing the result to project window

myTime()
root.mainloop()
