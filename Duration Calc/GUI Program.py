from tkinter import *


def calc_time_in_min():
    new_duration = float(time_input.get()) / float(speed_input.get())
    rounded_val = round(new_duration, 2)
    result_label.config(text=f"{rounded_val}")


window = Tk()
window.title("Duration Calculator")
window.config(width=800, height=300, padx=20, pady=20)

speed_label = Label(text="Speed: ")
speed_label.grid(column=0, row=0)

speed_input = Entry()
speed_input.config(width=8)
speed_input.grid(column=1, row=0)

time_label = Label(text="Time: ")
time_label.grid(column=0, row=1)

new_time_button = Button(text="New Time: ", command=calc_time_in_min)
new_time_button.grid(column=0, row=2)

time_input = Entry()
time_input.config(width=8)
time_input.grid(column=1, row=1)

result_label = Label(text="Output")
result_label.grid(column=1, row=2)

min_label1 = Label(text="min")
min_label1.grid(column=2 , row=1)

min_label2 = Label(text="min")
min_label2.grid(column=2, row=2)


window.mainloop()
