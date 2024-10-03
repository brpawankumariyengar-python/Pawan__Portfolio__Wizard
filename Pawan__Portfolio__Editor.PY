import json
import tkinter as tk
from tkinter import ttk

from tkinter import messagebox as Pawan__Messagebox
import re

# Global variable to hold the main dictionary
Pawan__List__URL = []
Pawan__List__Number__Of__Shares = []
Pawan__List__Total__Amount = []
Pawan__Bool__Is__New__Share = False

def Pawan__Load__Data():
    """
    Function to load data from a file and parse it as JSON.
    """
    global Pawan__List__URL
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global Pawan__Main__Dictionary 
    with open("Pawan__Portfolio__Wizard.FOOD", 'r') as File__Data:
        Pawan__Main__Dictionary = json.loads(File__Data.read())
    Pawan__List__URL = [Pawan__Main__Dictionary[Item][0] for Item in Pawan__Main__Dictionary]
    Pawan__List__Number__Of__Shares = [Pawan__Main__Dictionary[Item][1] for Item in Pawan__Main__Dictionary]
    Pawan__List__Total__Amount = [Pawan__Main__Dictionary[Item][2] for Item in Pawan__Main__Dictionary]

def Pawan___Add__window():
    """
    Function to open a new window for adding data.
    Replaces the dropdown with a textbox and changes buttons.
    """
    global Pawan__List__URL
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global edit_button
    global delete_button
    global add_button
    global new_window
    global url_entry
    global entry2
    global entry3
    global Pawan__Bool__Is__New__Share

    Pawan__Bool__Is__New__Share = True

    edit_button.config(state='disabled')
    delete_button.config(state='disabled')
    add_button.config(state='disabled')
    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Add a new company to your portfolio")
    new_window.geometry("900x250")  # Setting the initial size of the window
    new_window.resizable(False, False)  # Disables resizing of the window

    # Label and Textbox (Replacing dropdown)
    label1 = tk.Label(new_window, text="Enter URL String:")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    url_entry = tk.Entry(new_window, width=100)
    url_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Label and Textbox 1
    label2 = tk.Label(new_window, text="Add a new company to your portfolio", font=("Verdana", 20))
    label2.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Label and Textbox 2
    label3 = tk.Label(new_window, text="Number Of Shares:")
    label3.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    entry2 = tk.Entry(new_window, width=100)
    entry2.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Label and Textbox 3
    label4 = tk.Label(new_window, text="Total Invested Amount:")
    label4.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    entry3 = tk.Entry(new_window, width=100)
    entry3.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Buttons in the new window
    submit_button = tk.Button(new_window, text="Submit", bg="lime", width=10, command = Pawan__Submit__New__Data)
    submit_button.grid(row=4, column=1, padx=10, pady=20)

    cancel_button = tk.Button(new_window, text="Cancel", bg="red", width=10, command=Pawan__Cancel__Process)
    cancel_button.grid(row=4, column=2, padx=10, pady=20)

def Pawan__Edit__window():
    """
    Function to open a new window for adding data.
    Replaces the dropdown with a textbox and changes buttons.
    """
    global url_dropdown
    global Number__Of__Shares__Text
    global Invested__Amount__Text
    global Pawan__List__URL
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global edit_button
    global delete_button
    global add_button
    global new_window
    global url_entry
    global entry2
    global entry3
    global Pawan__Bool__Is__New__Share

    Pawan__Bool__Is__New__Share = False

    edit_button.config(state='disabled')
    delete_button.config(state='disabled')
    add_button.config(state='disabled')
    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Edit an existing Company in your portfolio")
    new_window.geometry("900x250")  # Setting the initial size of the window
    new_window.resizable(False, False)  # Disables resizing of the window

    # Label and Textbox (Replacing dropdown)
    label1 = tk.Label(new_window, text="Enter URL String:")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    url_entry = tk.Entry(new_window, width=100)
    url_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Label and Textbox 1
    label2 = tk.Label(new_window, text="Edit an existing Company in your portfolio", font=("Verdana", 20))
    label2.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Label and Textbox 2
    label3 = tk.Label(new_window, text="Number Of Shares:")
    label3.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    entry2 = tk.Entry(new_window, width=100)
    entry2.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Label and Textbox 3
    label4 = tk.Label(new_window, text="Total Invested Amount:")
    label4.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    entry3 = tk.Entry(new_window, width=100)
    entry3.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    url_entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    url_entry.insert(0, url_dropdown.get())
    entry2.insert(0, Number__Of__Shares__Text.get())
    entry3.insert(0, Invested__Amount__Text.get())

    # Buttons in the new window
    submit_button = tk.Button(new_window, text="Submit", bg="lime", width=10, command = Pawan__Submit__New__Data)
    submit_button.grid(row=4, column=1, padx=10, pady=20)

    cancel_button = tk.Button(new_window, text="Cancel", bg="red", width=10, command=Pawan__Cancel__Process)
    cancel_button.grid(row=4, column=2, padx=10, pady=20)


def Pawan__Cancel__Process():
    global edit_button
    global delete_button
    global add_button
    global new_window

    edit_button.config(state='normal')
    delete_button.config(state='normal')
    add_button.config(state='normal')

    new_window.destroy()

def Pawan__Gather__Data():
	global url_dropdown
	global Number__Of__Shares__Text
	global Invested__Amount__Text
	global Pawan__List__URL
	global Pawan__List__Number__Of__Shares
	global Pawan__List__Total__Amount
	global edit_button
	global delete_button
	global add_button
	popo = url_dropdown.get()
	Index = Pawan__List__URL.index(popo)
	lolo = Pawan__List__Number__Of__Shares[Index]
	koko = Pawan__List__Total__Amount[Index]
	Number__Of__Shares__Text.delete(0, tk.END)
	Invested__Amount__Text.delete(0, tk.END)
	Number__Of__Shares__Text.insert(0, lolo)
	Invested__Amount__Text.insert(0, koko)

def Pawan__Delete__Data():
    global Pawan__List__URL
    global Pawan__Main__Dictionary
    global url_dropdown
    global Number__Of__Shares__Text
    global Invested__Amount__Text
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global edit_button
    global delete_button
    global add_button
    Pawan__Record__Response = Pawan__Messagebox.askokcancel("Confirm Data Delete", f"Please confirm that you want to delete {url_dropdown.get()} from your portfolio. Kindly Note that this is not recoverable. Please click on OK to delete data")
    if Pawan__Record__Response:
        popo = url_dropdown.get()
        for temp_Key, temp_value in Pawan__Main__Dictionary.items():
            if popo == temp_value[0]: my_Key = temp_Key
        del Pawan__Main__Dictionary[my_Key]
        new_dict = {}
        for index, (key, value) in enumerate(Pawan__Main__Dictionary.items(), start=1):
            new_dict[index] = value
        Pawan__Main__Dictionary = new_dict
        with open("Pawan__Portfolio__Friend.FOOD", 'w') as File__Data:
            json.dump(Pawan__Main__Dictionary, File__Data, indent=4)



def Pawan__Launch__GUI():
    global Pawan__List__URL
    global url_dropdown
    global Number__Of__Shares__Text
    global Invested__Amount__Text
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global edit_button
    global delete_button
    global add_button

    # Create the main window
    root = tk.Tk()
    root.title("Custom GUI")
    root.geometry("900x250")  # Setting the initial size of the window
    root.resizable(False, False)  # Disables resizing of the window

    # Adjust column weights for even button spacing
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Create labels and inputs

    # Top Label with Dropdown
    URL__Label = tk.Label(root, text=" URL String:")
    URL__Label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    # Dropdown (Combobox)
    url_var = tk.StringVar()
    url_dropdown = ttk.Combobox(root, textvariable=url_var, width=100)
    url_dropdown['values'] = Pawan__List__URL
    url_dropdown.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='w')
    # Bind the selection event to the Pawan__Gather__Data function
    url_dropdown.bind("<<ComboboxSelected>>", lambda event: Pawan__Gather__Data())

    # Label and Textbox 1
    Main__Title  = tk.Label(root, text="See the current companies in your portfolio", font=("Verdana", 20))
    Main__Title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Label and Textbox 2
    Number__Of__Shares = tk.Label(root, text="Number Of Shares:")
    Number__Of__Shares.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    Number__Of__Shares__Text = tk.Entry(root, width=100)
    Number__Of__Shares__Text.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Label and Textbox 3
    Invested__Amount = tk.Label(root, text="Total Invested Amount:")
    Invested__Amount.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    Invested__Amount__Text = tk.Entry(root, width=100)
    Invested__Amount__Text.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='w')


    # Buttons
    edit_button = tk.Button(root, text="Edit", bg="yellow", width=10, command=Pawan__Edit__window)
    edit_button.grid(row=4, column=0, padx=40, pady=20)

    delete_button = tk.Button(root, text="Delete", bg="red", width=10, command = Pawan__Delete__Data)
    delete_button.grid(row=4, column=1, padx=0, pady=20)

    add_button = tk.Button(root, text="Add", bg="lime", width=10, command=Pawan___Add__window)
    add_button.grid(row=4, column=2, padx=10, pady=20)

    # Run the GUI loop
    root.mainloop()

def Pawan__Submit__New__Data():
    Pawan__Integer__Pattern = re.compile(r'^\d+$')
    Pawan__Float__Pattern = re.compile(r'^\d+\.*\d+$')
    Pawan__URL__Pattern = re.compile(r'^https://www\.bseindia\.com/stock-share-price/[^/]*[^/]+/.*/5\d{5}/$')
    global url_entry
    global entry2
    global entry3
    global Pawan__Bool__Is__New__Share
    global Pawan__List__URL
    global Pawan__List__Number__Of__Shares
    global Pawan__List__Total__Amount
    global new_window
    popo = url_entry.get()
    lolo = entry2.get()
    koko = entry3.get()
    if Pawan__Bool__Is__New__Share == True and popo in Pawan__List__URL:
        Pawan__Messagebox.showerror("Share Already in Portfolio", "The Share that you are trying to add is already in your portfolio. Please use the edit option to edit the number of shares. Same company cannot be added twice.")
        url_entry.delete(0, tk.END)
    else:
        if bool(Pawan__URL__Pattern.match(popo)) == True:
            if bool(Pawan__Float__Pattern.match(koko)) == True:
                if bool(Pawan__Integer__Pattern.match(lolo)) == True:
                    if koko.find(".") == -1:
                        koko = koko + ".00"
                    Pawan__List__URL.append(popo)
                    Pawan__List__Number__Of__Shares.append(lolo)
                    Pawan__List__Total__Amount.append(koko)
                    Pawan__Messagebox.showinfo("Data Updated", f"Data has been updated as URL {popo} \nNumber Of shares {lolo} \nTotal invested amount {koko}")
                    Pawan__Update__Dictionary__and__File(popo, lolo, koko)
                    Pawan__Bool__Is__New__Share = False
                    Pawan__Cancel__Process()
                else:
                    Pawan__Messagebox.showerror("Incorrect input for Number of shares", "The number of shares should be entered in digits from 0-9 with no spaces or commas or any other charecters. Only digits are accepted")
                    entry2.delete(0, tk.END)
                    new_window.lift()
                    new_window.attributes('-topmost', True)
            else:
                Pawan__Messagebox.showerror("Incorrect input for Total Amount Invested", "The number of shares should be entered in float format consiting of digits from 0-9 and a single period // dot (.). No or commas or any other charecters are accepted. Only digits are accepted")
                entry3.delete(0, tk.END)
                new_window.lift()
                new_window.attributes('-topmost', True)
        else:
            Pawan__Messagebox.showerror("Incorrect input for BSE URL", "The URL entered should be for stocks lisdted on BSE (Bombay Stock Exchange) and should be picked up after searching the company on BSE. Please recheck the URL as IT does not match BSE URL pattern.")
            url_entry.delete(0, tk.END)
            new_window.lift()
            new_window.attributes('-topmost', True)

def  Pawan__Update__Dictionary__and__File(popo, lolo, koko):
    global Pawan__Main__Dictionary
    if Pawan__Bool__Is__New__Share == True:
        last_key = len(Pawan__Main__Dictionary)
        my_Key = str(int(last_key) + 1)
    else:
        for temp_Key, temp_value in Pawan__Main__Dictionary.items():
            if popo == temp_value[0]: my_Key = temp_Key
    Pawan__Main__Dictionary[my_Key] = [popo, int(lolo), float(koko)]
    with open("Pawan__Portfolio__Friend.FOOD", 'w') as File__Data:
        json.dump(Pawan__Main__Dictionary, File__Data, indent=4)


if __name__ == "__main__":
    Pawan__Load__Data()
    Pawan__Launch__GUI()





