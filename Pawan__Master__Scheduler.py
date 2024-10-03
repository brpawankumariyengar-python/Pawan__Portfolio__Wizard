from tkinter import *
from tkinter import messagebox as Vachak
from datetime import datetime as Samay
import subprocess as Sevak
from Pawan__PDF__Generator import Pawan__Graph__Generation__Operation
import os as Prachalan__Pranali

Pawan__Root = Tk()
Pawan__Root.iconbitmap("Icon.ico")
Pawan__Root.title("Pawan Portfolio Wizard")

Ctr = 0

Pawan__Set__Day = "Sunday"
Pawan__Set__Hour = "01"
Pawan__Set__Minute = "01"
Pawan__Set__Am__PM = "AM"
Pawan__Execute__Schedule = True

Pawan__Folder__Path = Prachalan__Pranali.getcwd()
Pawan__Folder__Path = Pawan__Folder__Path  + "\\Images\\"

# Global variables to capture the selected values
selected_day = StringVar(value="Sunday")
hour_var = StringVar(value="01")
am_pm_var = StringVar(value="AM")
minute_var = StringVar(value="01")

def Pawan__Main__Window():
    Pawan__Root.geometry("300x200") 
    global Pawan__Button__Change__Schedule
    global Pawan__Button__Pause
    global Pawan__Button__Show__Schedule
    
    # Create a grid with 3 columns to center the widgets
    Pawan__Root.grid_columnconfigure(0, weight=1)
    Pawan__Root.grid_columnconfigure(1, weight=1)
    Pawan__Root.grid_columnconfigure(2, weight=1)
    
    # Main Window Widgets
    Pawan__Title__Label = Label(Pawan__Root, text = "Pawan Master Scheduler for Weekly Reports")
    Pawan__Button__Change__Schedule = Button(Pawan__Root, text = "Change Existing Schedule", command=Pawan__Show__Schedule__Options)
    Pawan__Button__Change__Schedule.config(bg='cyan')
    Pawan__Button__Pause = Button(Pawan__Root, text = "Pause Schedule Execution", command = Pawan__Pause__Schedule__Excution)
    Pawan__Button__Pause.config(bg='red')
    Pawan__Button__Resume = Button(Pawan__Root, text = "Resume Schedule Execution", command = Pawan__Resume__Schedule__Excution)
    Pawan__Button__Resume.config(bg='green')
    Pawan__Button__Show__Schedule = Button(Pawan__Root, text = "Show Schedule", command = Pawan__Show__Execution__Schedule)
    Pawan__Button__Show__Schedule.config(bg='yellow')
    
    # Positioning Widgets Using Grid
    Pawan__Title__Label.grid(row=0, column=0, columnspan=3, pady=10)
    Pawan__Button__Change__Schedule.grid(row=1, column=1, pady=5)
    Pawan__Button__Show__Schedule.grid(row=2, column=1, pady=5)
    Pawan__Button__Pause.grid(row=3, column=1, pady=5)
    Pawan__Button__Resume.grid(row=4, column=1, pady=5)
    
    Pawan__Root.resizable(0,0)
    Pawan__Root.mainloop()

def Pawan__Show__Schedule__Options():
    global Pawan__Button__Change__Schedule
    global Pawan__Button__Pause

    # Disable Change Schedule Till Submit Button is pressed
    Pawan__Button__Change__Schedule.config(state=DISABLED)
    Pawan__Button__Pause.config(state=DISABLED)

    # Get the current width and height of the window
    current_width = Pawan__Root.winfo_width()
    current_height = Pawan__Root.winfo_height()
    
    # Multiply the current dimensions
    new_width = current_width * 2
    new_height = current_height * 3
    
    # Set the new window size
    Pawan__Root.geometry(f"{new_width}x{new_height}")
    
    # Clear the previous grid configuration
    for widget in Pawan__Root.winfo_children():
        widget.grid_forget()

    # Configure new grid
    Pawan__Root.grid_columnconfigure(0, weight=1)
    Pawan__Root.grid_columnconfigure(1, weight=1)
    Pawan__Root.grid_columnconfigure(2, weight=1)

    # Label above radio buttons
    Pawan__Radio_Label = Label(Pawan__Root, text="Select a Day:")
    Pawan__Radio_Label.grid(row=0, column=1, pady=10)

    # Add the radio buttons for days of the week, defaulting to "Sunday"
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for i, day in enumerate(days):
        radio_button = Radiobutton(Pawan__Root, text=day, variable=selected_day, value=day)
        radio_button.grid(row=i+1, column=1, pady=2)
    
    # Create labels for dropdowns
    Pawan__Label_Hour = Label(Pawan__Root, text="Hour:")
    Pawan__Label_AM_PM = Label(Pawan__Root, text="AM/PM:")
    Pawan__Label_Minute = Label(Pawan__Root, text="Minute:")
    

    # Create dropdowns for Hours, AM/PM, and Minutes
    hours = [f"{str(h).zfill(2)}" for h in range(1, 13)]  # Options from 01 to 12
    am_pm = ["AM", "PM"]        # AM/PM options
    minutes = [f"{str(m).zfill(2)}" for m in range(0, 60)]  # Options from 00 to 59
    
    hour_dropdown = OptionMenu(Pawan__Root, hour_var, *hours)
    am_pm_dropdown = OptionMenu(Pawan__Root, am_pm_var, *am_pm)
    minute_dropdown = OptionMenu(Pawan__Root, minute_var, *minutes)

    # Positioning Labels and Dropdowns Using Grid
    Pawan__Label_Hour.grid(row=len(days)+1, column=0, sticky=E, padx=10, pady=5)
    hour_dropdown.grid(row=len(days)+1, column=1, pady=5)
    
    Pawan__Label_AM_PM.grid(row=len(days)+3, column=0, sticky=E, padx=10, pady=5)
    am_pm_dropdown.grid(row=len(days)+3, column=1, pady=5)
    
    Pawan__Label_Minute.grid(row=len(days)+2, column=0, sticky=E, padx=10, pady=5)
    minute_dropdown.grid(row=len(days)+2, column=1, pady=5)
    
    # Add the "Submit Change Schedule" button at the end
    Pawan__Button__Submit__Schedule = Button(Pawan__Root, text="Submit Change Schedule", command=Pawan__Submit__Change__Schedule)
    Pawan__Button__Submit__Schedule.config(bg='lime')
    Pawan__Button__Submit__Schedule.grid(row=len(days)+4, column=1, pady=10)

def Pawan__Submit__Change__Schedule():
    global Pawan__Set__Day
    global Pawan__Set__Hour
    global Pawan__Set__Minute
    global Pawan__Set__Am__PM
    # Capture the selected values
    Pawan__Set__Day = selected_day.get()
    Pawan__Set__Hour = hour_var.get()
    Pawan__Set__Am__PM = am_pm_var.get()
    Pawan__Set__Minute = minute_var.get()

    # Show the captured values (for debugging or further processing)
    Vachak.showinfo("The execution scheduled has been set" , f"The execution schedule has been set to {Pawan__Set__Day} of every week at {Pawan__Set__Hour}:{Pawan__Set__Minute} {Pawan__Set__Am__PM}")
    
    # Clear all widgets and go back to the main window
    for widget in Pawan__Root.winfo_children():
        widget.destroy()
    Pawan__Main__Window()

def Pawan__Pause__Schedule__Excution():
    global Pawan__Execute__Schedule
    Pawan__Execute__Schedule = False
    Vachak.showinfo("Scheduled report generation paused","The execution of scheduled report generation has been paused")

def Pawan__Resume__Schedule__Excution():
    global Pawan__Execute__Schedule
    Pawan__Execute__Schedule = True
    Vachak.showinfo("Scheduled report generation resumed","The execution of scheduled report generation has been resumed")

def Pawan__Show__Execution__Schedule():
    Vachak.showinfo("Current Selected Schedule",f"The execution of scheduled report generation has been set for {Pawan__Set__Day} of every week at {Pawan__Set__Hour}:{Pawan__Set__Minute} {Pawan__Set__Am__PM}")

def Pawan__Check__Time():
    global Pawan__Set__Day
    global Pawan__Set__Hour
    global Pawan__Set__Minute
    global Pawan__Set__Am__PM
    global Pawan__Execute__Schedule
    global Ctr
    Pawan__Current__Date__Time = Samay.now()
    Pawan__Hour = Pawan__Current__Date__Time.strftime("%I")
    Pawan__Weekday = Pawan__Current__Date__Time.strftime("%A")
    Pawan__Minute = Pawan__Current__Date__Time.strftime("%M")
    Pawan__AM__PM = Pawan__Current__Date__Time.strftime("%p")

    if Pawan__Execute__Schedule == True:
        if Pawan__Weekday == Pawan__Set__Day and Pawan__Hour == Pawan__Set__Hour and Pawan__Minute == Pawan__Set__Minute and Pawan__AM__PM == Pawan__Set__Am__PM:
            Pawan__Execute__Schedule = False
            Pawan__Main__Execution__Process()
    Pawan__Root.after(10000, Pawan__Check__Time)


def Pawan__Main__Execution__Process():
    global Pawan__Execute__Schedule
    Vachak.showinfo("The main execution process has started", "The main execution process has been started as per schedule. The application shall now scrape the BSE (Bombay Stock Exchange) and will gather all data as per your portfolio. Then as per the generated output graphs will be generated and placed in a PDF document that you can use to analyse the portfolio.")
    Vachak.showinfo("The process may take up to an hour to complete", "The process needs time to execution as the website may take time to load and then we have scrape and gather all data. This is a time consuming process and as per a regular portfolio of between 15 to 20 shares, the overall process may take an hour.")
    result = Sevak.run(['python', 'Pawan__Portfolio__Wizard.PY'], capture_output=True, text=True)
    result = Sevak.run(['python', 'Pawan__Images__To__Text.PY'], capture_output=True, text=True)
    result = Sevak.run(['python', 'Pawan__Excel__Spreadsheet__Generator.PY'], capture_output=True, text=True)
    if result.stderr == "": 
        Vachak.showinfo("No errors detected.", "No errors were encountered and we have a successful execution of web scrapping.")
        Pawan__Execute__Schedule = True
        Pawan__Excel__Filename =  "Pawan__Portfolio__Wizard.xlsx"
        current_directory = Prachalan__Pranali.getcwd()
        Pawan__Current__Directory__Content = Prachalan__Pranali.listdir(current_directory)
        for index, item in enumerate(Pawan__Current__Directory__Content):
            Pawan__Current__Directory__Content[index] = item
        if Pawan__Excel__Filename in Pawan__Current__Directory__Content:
            Vachak.showinfo("Excel File Created", f"Excel File {Pawan__Excel__Filename} has been successfully created and is ready for further processing.")
            Pawan__Run__Graph__Generation()
        else:  Vachak.showerror("Excel file not found Error", f"Excel File {Pawan__Excel__Filename} is not found. Please restart the application and re-run the execution.")
    else: Vachak.showinfo("Errors :\n", result.stderr)

    
def Pawan__Run__Graph__Generation():
    global Pawan__Folder__Path

    Vachak.showinfo("Starting the generation of graphs", "Starting the generation of graphs and this process takes 15 - 20 minutes based upon average portfolio of 15 to 20 shares.")
    result = Sevak.run(['python', 'Pawan__Graph__Generator.PY'], capture_output=True, text=True)
    if result.stderr == "": 
        Vachak.showinfo("No errors detected.", "No errors were encountered and we have a successful execution of Graph Generation.")
    else: Vachak.showinfo("Errors :\n", result.stderr)

    Pawan__Current__Directory__Content = Prachalan__Pranali.listdir(Pawan__Folder__Path)

    Pawan__PNG__Filename1 = "01__Total__Asset__Value.png"
    Pawan__PNG__Filename2 = "02__Percentage__Of__Investment__Per__Share__Category.png"
    Pawan__PNG__Filename3 = "03__Profit__&__Loss__Per__Stock.png"
    Pawan__PNG__Filename4 = "04__Profit_Loss_Percentage.png"
    Pawan__PNG__Filename5 = "05__ROE__Information.png"
    Pawan__PNG__Filename6 = "06__EPS__Information.png"
    Pawan__PNG__Filename7 = "07__PB__Ratio__Information.png"
    Pawan__PNG__Filename8 = "08__PE__Ratio__Information.png"


    if Pawan__PNG__Filename1 in Pawan__Current__Directory__Content:
        if Pawan__PNG__Filename2 in Pawan__Current__Directory__Content:
            if Pawan__PNG__Filename3 in Pawan__Current__Directory__Content:
                if Pawan__PNG__Filename4 in Pawan__Current__Directory__Content:
                    if Pawan__PNG__Filename5 in Pawan__Current__Directory__Content:
                        if Pawan__PNG__Filename6 in Pawan__Current__Directory__Content:
                            if Pawan__PNG__Filename7 in Pawan__Current__Directory__Content:
                                if Pawan__PNG__Filename8 in Pawan__Current__Directory__Content:
                                    Vachak.showinfo("All Graphs Created", "All the graphs from the data obtained have been successfully created as PNG files and are ready for further processing.")
                                    Pawan__PDF__Generation(Pawan__Current__Directory__Content)
                                else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename8 } is not found. Please restart the application and re-run the execution.")
                            else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename7 } is not found. Please restart the application and re-run the execution.")
                        else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename6 } is not found. Please restart the application and re-run the execution.")
                    else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename5 } is not found. Please restart the application and re-run the execution.")
                else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename4 } is not found. Please restart the application and re-run the execution.")
            else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename3 } is not found. Please restart the application and re-run the execution.")
        else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename2 } is not found. Please restart the application and re-run the execution.")
    else: Vachak.showerror("PNG file not found Error", f"PNG File {Pawan__PNG__Filename1 } is not found. Please restart the application and re-run the execution.")

def Pawan__PDF__Generation(Pawan__Current__Directory__Content):
    Vachak.showinfo("PDF File Generation Starting","Thank you for being so patient. We are now in the final phase of PDF File Generation. Hopefully we will be done soon.")
    Pawan__Graph__Generation__Operation()

    Prachalan__Pranali.remove(Pawan__Folder__Path + "01__Total__Asset__Value.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "02__Percentage__Of__Investment__Per__Share__Category.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "03__Profit__&__Loss__Per__Stock.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "04__Profit_Loss_Percentage.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "05__ROE__Information.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "06__EPS__Information.png")
    Prachalan__Pranali.remove(Pawan__Folder__Path + "07__PB__Ratio__Information.png")
    Prachalan__Pranali.remove("Pawan__Portfolio__Wizard.xlsx")
    for file_name in Prachalan__Pranali.listdir(Pawan__Folder__Path):
        file_path = Prachalan__Pranali.path.join(Pawan__Folder__Path, file_name)
        if Prachalan__Pranali.path.isfile(file_path):
            try:
                Prachalan__Pranali.remove(file_path)
            except Exception as e:
                Vachak.showerror("Could Not Delete Files. Error Faced.", f"Error deleting file {file_path}: {e}")


    try: 
        Prachalan__Pranali.rmdir(Pawan__Folder__Path)
    except Exception as e:
        Vachak.showerror("Could Not Delete Folder. Error Faced.", f"Error deleting folder {Pawan__Folder__Path}: {e}")


if __name__ == "__main__":
    Pawan__Root.after(10000, Pawan__Check__Time)
    Pawan__Main__Window()

