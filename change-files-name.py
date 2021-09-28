
# the Most important modules
import os
from tkinter import *
# Create The main Window
window = Tk()
# to size the main Screen
window.geometry("600x300")
# Change the Title
window.title("Rename Files :")
# To Prevint the resize
window.resizable(0, 0)
# The Variable we used
pady5 = 5
hi_clr = "red"
hi_bg = "#ddd"
main_clr = "#1e3a1e"
# Create The Logic


# Restarts the Whole Window
def restart():
    """
    Function to Restart the window application 
    """
    window.destroy()
    os.system(r"F:\WEB-Devolopment\python\change-files-name.py")


count_click = 2


def rename_files():
    """
    The main Function to remove the starter string you dont want
    and this string in first name of files
    """
    try:
        get_folder_path = folder_path.get()
        get_will_remove = will_remove.get()
        list_folder_path = os.listdir(get_folder_path)
        referance_word = get_will_remove[0:3]
        if get_will_remove != "":
            for file in list_folder_path:
                if str(file).startswith(referance_word):
                    os.rename(rf"{get_folder_path}\{file}",
                              rf"{get_folder_path}\{file[len(get_will_remove):]}")
            footer_lbl = Label(window, text="Done............",
                               font=("Arial", 12, "normal"), fg=main_clr)
            footer_lbl.pack()
        else:
            footer_lbl = Label(window, text="Please Write The Word to Remove",
                               font=("Arial", 12, "normal"), fg="red")
            footer_lbl.pack()
            # condition to restart the program after number of trys
            global count_click
            count_click -= 1
            if count_click == 0:
                restart()

    except FileNotFoundError:
        footer_lbl = Label(window, text="File Not Found Please Check Your Path",
                           font=("Arial", 12, "normal"), fg="red")
        footer_lbl.pack()
        # condition to restart the program after number of trys
        count_click -= 1
        if count_click == 0:
            restart()


# The Main Label
lbl1 = Label(window, text="Wellcome To Rename Files", font=(
    "Atial", 12, "bold"), fg=main_clr).pack(side="top", pady=pady5)
########################################
# Create Fram as first feild container
fram1 = Frame(window, width=600, height=50, bd=0, highlightbackground=hi_bg,
              highlightthickness=2, highlightcolor=hi_clr)
fram1.pack(side="top", pady=pady5)
# --------------------------------------------
# To connect Entry With String
folder_path = StringVar()
folder_path.set(value=r"C:\Users\Mazen Essam\Desktop\kitchens")
lbl1 = Label(fram1, text="Write your directory Path:", width=22,
             height=2, font=("Arial", 13, "bold"), bd=0)
lbl1.grid(
    row=0, column=0)
# --------------------------------------------
entry1 = Entry(fram1, width=51, textvariable=folder_path,
               font=("Arial", 10, "normal"))
entry1.grid(row=0, column=1, padx=7, ipady=7)
########################################
# Create Fram as Second feild container
fram2 = Frame(window, width=600, height=50, bd=0, highlightbackground=hi_bg,
              highlightthickness=2, highlightcolor=hi_clr)
fram2.pack(side="top", pady=pady5)
# --------------------------------------------
# To connect Entry With String
will_remove = StringVar()
# will_remove.set(value="What You Wont To Clear")
lbl2 = Label(fram2, text="Value To Remove:", width=15,
             height=2, font=("Arial", 13, "bold"), bd=0)
lbl2.grid(
    row=0, column=0)
# --------------------------------------------
entry2 = Entry(fram2, width=61, textvariable=will_remove,
               font=("Arial", 10, "normal"))
entry2.grid(row=0, column=1, padx=7, ipady=7)
#########################################
# Create Fram as Button container
fram3 = Frame(window, width=600, height=50, bd=0, highlightbackground=hi_bg,
              highlightthickness=2, highlightcolor=hi_clr)
fram3.pack(side="top", pady=pady5)
btn = Button(fram3, text="Click To Rename", width=15, height=1, font=(
    "Arial", 15, "bold"), bd=1, bg=main_clr, fg="#fff", command=lambda: rename_files())
btn.pack(ipady=10, pady=0)
window.mainloop()
