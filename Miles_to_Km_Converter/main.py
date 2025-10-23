from tkinter import *

window  =   Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)
#We can also add padding around any object:
window.config(padx=50, pady=50)

km = 0

def mile_to_km():
    miles = int(entry.get())
    km  = miles * 1.609
    my_label_3.config(text=km)





my_label_1 = Label(text="Miles", font=("Arial", 14))
my_label_1.grid(column=2, row=0)

my_label_2 = Label(text="is equal to", font=("Arial", 14))
my_label_2.grid(column=0, row=1)


my_label_3 = Label(text=f"{km}", font=("Arial", 14))
my_label_3.grid(column=1, row=1)


my_label_4 = Label(text="Km", font=("Arial", 14))
my_label_4.grid(column=2, row=1)


button = Button(text="Calculate", command=mile_to_km)
# button.pack()
button.grid(column=1, row=2)

entry = Entry(width=10)
#input.pack()
entry.grid(column=1, row=0)



















window.mainloop()