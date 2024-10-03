import pytesseract
import os as Prachalan__Pranali
import glob as Sadhakah
import time

def Pawan__Create__Image__List():
	Pawan__Folder__Path = Prachalan__Pranali.getcwd()
	Pawan__Folder__Path = Pawan__Folder__Path  + "\\Images\\"
	Pawan__Serarch__Pattern = Prachalan__Pranali.path.join(Pawan__Folder__Path,"*.png")
	Pawan__List__Image__Files = Sadhakah.glob(Pawan__Serarch__Pattern)
	for Pawan__Captured__Image in Pawan__List__Image__Files:
		Pawan__OCR__From__Image(Pawan__Captured__Image)



def Pawan__OCR__From__Image(Pawan__Captured__Image):
    Pawan__OCR__Text =""
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    # Perform OCR on the image
    Pawan__OCR__Text = pytesseract.image_to_string(Pawan__Captured__Image)
    Text__File__Name = Pawan__Captured__Image[:-3:] + "txt"
    with open(Text__File__Name, 'w') as File__Data:
    	File__Data.write(Pawan__OCR__Text)


if __name__ == "__main__":
	Pawan__Create__Image__List()
	time.sleep(11)