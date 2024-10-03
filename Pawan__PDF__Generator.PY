from fpdf import FPDF as PDF__Generation__Package
from fpdf.enums import XPos, YPos  # Correct enums import
import easygui as Pawan__GUI__Box
import os as Prachalan__Pranali

#FPDF Options
#Layout ('P', 'L')
#Unit ('mm', 'cm', 'in')
#Format ('A3', 'A4', 'A5', '(default)', 'Letter', 'Legal, ('100,150')) #Please Note: format ('100,150') is user choice or custom format

def Pawan__Graph__Generation__Operation():
    Pawan__PDF__Document = PDF__Generation__Package('P', 'mm', 'A4')
    Pawan__PDF__Document.add_page()

    #Specify Fonts
    #Fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
    #Font Types ('B' for bold, 'I' for Italics, 'U' for underline, '' for regular, or combination  Example: 'BU' for bold and underline)
    Pawan__PDF__Document.set_font('helvetica', '', 16) # here 16 is the font size

    #To add text we can use cell (single line of text) or multi cell (for multiple lines
    # Cell has width and Height to be set. Setting width to zero (0) will cause the cell to go page width.
    #we create the cell as cell(Width, height, text)

    Pawan__Folder__Path = Prachalan__Pranali.getcwd()
    Pawan__Folder__Path = Pawan__Folder__Path  + "\\Images\\"

    Pawan__PDF__Document.cell(40, 10, "This is a python Generated Portfolio Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT) # Move to the next line
    #Using new_x and new_y: Replaced ln=True with new_x=XPos.LMARGIN and new_y=YPos.NEXT. This tells the fpdf library to move to the left margin (LMARGIN) and to the next line (NEXT).
    Pawan__PDF__Document.cell(40, 10, "Below are the graphs to explain Portfolio in detail")
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "01__Total__Asset__Value.png", 10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "02__Percentage__Of__Investment__Per__Share__Category.png",  10, 30, 210) #here I am not incrseing the height of the graph as the circle becomes egg shaped
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "03__Profit__&__Loss__Per__Stock.png",  10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "04__Profit_Loss_Percentage.png",  10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "05__ROE__Information.png",  10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "06__EPS__Information.png",  10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "07__PB__Ratio__Information.png",  10, 30, 210, 170)
    Pawan__PDF__Document.add_page()
    Pawan__PDF__Document.image(Pawan__Folder__Path  + "08__PE__Ratio__Information.png",  10, 30, 210, 170)

    filename = Pawan__GUI__Box.filesavebox(msg="Save the generated PDF File", title="Save PDF File As", default="My__Portfolio__Report.pdf", filetypes=["*.pdf"])
    filename = filename + ".PDF"
    Pawan__PDF__Document.output(filename) # Here we use output to generate the PDF

if __name__ == "__main__":
    Pawan__Graph__Generation__Operation()