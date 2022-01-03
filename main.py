from tkinter import *
import tkinter.messagebox
import back

# creating the app
root = Tk()
root.geometry("600x500")
root.configure(bg="ghost white")
# root.iconbitmap("logo.ico")
root.title("Cyberxploit Hausa Youtube manager")


date = StringVar()
vidID = StringVar()
vidTitle = StringVar()
vidType = StringVar()
status = StringVar()


def get_selected_tuple(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)

    date_entry.delete(0, END)
    date_entry.insert(END, selected_tuple[1])
    vidId_entry.delete(0, END)
    vidId_entry.insert(END, selected_tuple[2])
    vidTitle_entry.delete(0, END)
    vidTitle_entry.insert(END, selected_tuple[3])
    vidType_entry.delete(0, END)
    vidType_entry.insert(END, selected_tuple[4])
    status_entry.delete(0, END)
    status_entry.insert(END, selected_tuple[5])


# creating button functions that will be called when a button is pressed


def add():
    if len(date.get()) != 0:
        back.addRec(
            date.get(), vidID.get(), vidTitle.get(), vidType.get(), status.get()
        )
        listbox.delete(0, END)
        listbox.insert(
            END, (date.get(), vidID.get(), vidTitle.get(),
                  vidType.get(), status.get())
        )


def view():
    listbox.delete(0, END)
    for row in back.viewRec():
        listbox.insert(END, row, str(""))


def clear():
    date_entry.delete(0, END)
    vidId_entry.delete(0, END)
    vidTitle_entry.delete(0, END)
    vidType_entry.delete(0, END)
    status_entry.delete(0, END)


def update():
    if len(date.get()) != 0:
        back.deleteRec(selected_tuple[0])
    if len(date.get()) != 0:
        back.addRec(
            date.get(), vidID.get(), vidTitle.get(), vidType.get(), status.get()
        )
        listbox.delete(0, END)
        listbox.insert(END, date.get(), vidID.get(), vidTitle.get(), vidType)


def search():
    listbox.delete(0, END)
    for row in back.searchRec(
        date.get(), vidID.get(), vidTitle.get(), vidType.get(), status.get()
    ):
        listbox.insert(END, row, str(""))


def delete():
    if (len(date.get())) != 0:
        back.deleteRec(selected_tuple[0])
        clear()
        view()


def exit():
    exit = tkinter.messagebox.askyesno(
        "CyberXploit Hausa", "Confirm if you want to exit"
    )
    if exit > 0:
        root.destroy()
        return


# creating the MainFrame in order to fit in other  frames and widgets
main_frame = Frame(root, bg="Ghost white")
main_frame.grid()

title_frame = Frame(main_frame, bd=2, padx=118, pady=6, bg="red", relief=RIDGE)
title_frame.pack(side=TOP)

title_label = Label(
    title_frame, font=("arial", 30, "bold"), text="CyberXploit Hausa", bg="orange"
)
title_label.grid()

data_frame = Frame(
    main_frame, width=500, height=200, padx=5, pady=5, bg="Ghost white", relief=RIDGE
)
data_frame.pack(side=TOP)

data_frameleft = LabelFrame(
    data_frame,
    bd=1,
    width=400,
    height=200,
    padx=5,
    pady=5,
    bg="Ghost white",
    relief=RIDGE,
    font=("arial", 15, "bold"),
    text="Youtube Video Uploads \n",
)
data_frameleft.pack(side=TOP)

button_frame = Frame(
    data_frame, width=50, height=60, pady=3, padx=3, bg="Ghost white", relief=RIDGE
)
button_frame.pack(side=TOP)

textArea_frame = LabelFrame(
    main_frame,
    bd=1,
    width=400,
    height=200,
    padx=5,
    pady=5,
    bg="red",
    relief=RIDGE,
    font=("arial", 15, "bold"),
    text="Upload Details",
)
textArea_frame.pack(side=BOTTOM)

# creating labels and widgets

date_label = Label(
    data_frameleft,
    text="Date:",
    font=("consolas", 14, "bold"),
    padx=1,
    pady=1,
    bg="Ghost white",
)
date_label.grid(row=0, column=0, sticky="W")
date_entry = Entry(data_frameleft, font=(
    "arial", 12), textvariable=date, width=10)
date_entry.grid(row=0, column=1)

vidId_label = Label(
    data_frameleft,
    text="VidID:",
    font=("consolas", 14, "bold"),
    padx=1,
    pady=1,
    bg="Ghost white",
)
vidId_label.grid(row=0, column=2, sticky="W")
vidId_entry = Entry(data_frameleft, font=(
    "arial", 12), textvariable=vidID, width=10)
vidId_entry.grid(row=0, column=3)

vidTitle_label = Label(
    data_frameleft,
    text="VidTitle:",
    font=("consolas", 14, "bold"),
    padx=1,
    pady=1,
    bg="Ghost white",
)
vidTitle_label.grid(row=1, column=0, sticky="W")
vidTitle_entry = Entry(
    data_frameleft, font=("arial", 12), textvariable=vidTitle, width=10
)
vidTitle_entry.grid(row=1, column=1)

vidType_label = Label(
    data_frameleft,
    text="VidType:",
    font=("consolas", 14, "bold"),
    padx=1,
    pady=1,
    bg="Ghost white",
)
vidType_label.grid(row=1, column=2, sticky="W")
vidType_entry = Entry(
    data_frameleft, font=("arial", 12), textvariable=vidType, width=10
)
vidType_entry.grid(row=1, column=3)

status_label = Label(
    data_frameleft,
    text="Status:",
    font=("consolas", 14, "bold"),
    padx=1,
    pady=1,
    bg="Ghost white",
)
status_label.grid(row=2, column=0, sticky="W")
status_entry = Entry(data_frameleft, font=(
    "arial", 12), textvariable=status, width=10)
status_entry.grid(row=2, column=1)

# creating listbox and scrollbar
scrollbar = Scrollbar(textArea_frame)
scrollbar.grid(row=0, column=1, sticky="NS")

listbox = Listbox(
    textArea_frame,
    width=60,
    height=10,
    font=("helvetica", 10, "bold"),
    yscrollcommand=scrollbar.set(0, 1),
)
listbox.grid(row=0, column=0, padx=4)

scrollbar.config(command=listbox.yview())
listbox.bind("<<ListboxSelect>>", get_selected_tuple)

# creating the buttons widget
add_button = Button(
    button_frame,
    text="Add",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=add,
    bd=3,
)
add_button.grid(row=0, column=0)

view_button = Button(
    button_frame,
    text="View",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=view,
    bd=3,
)
view_button.grid(row=0, column=1)

clear_button = Button(
    button_frame,
    text="Clear",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=clear,
    bd=3,
)
clear_button.grid(row=0, column=2)

update_button = Button(
    button_frame,
    text="Update",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=update,
    bd=3,
)
update_button.grid(row=0, column=3)

search_button = Button(
    button_frame,
    text="Search",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=search,
    bd=3,
)
search_button.grid(row=0, column=4)

delete_button = Button(
    button_frame,
    text="Delete",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=delete,
    bd=3,
)
delete_button.grid(row=0, column=5)

exit_button = Button(
    button_frame,
    text="Exit",
    font=("courier", 10, "bold"),
    height=1,
    width=5,
    command=exit,
    bd=3,
)
exit_button.grid(row=0, column=6)

# calling the app to run from top to bottom

if __name__ == "__main__":
    root.mainloop()
