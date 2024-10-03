import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageEnhance
import io
import time
import os

def Pawan__Load__JSON():
	with open("Pawan__Portfolio__Wizard.FOOD", 'r') as Pawan__File__Data: Pawan__Share__Dictionary = json.load(Pawan__File__Data)
	Pawan__Loop__Dictionary(Pawan__Share__Dictionary)

def Pawan__Loop__Dictionary(Pawan__Share__Dictionary):
	Idhar = os.getcwd()
	folder__path = Idhar  + "\\Images\\"
	if not os.path.exists(folder__path): os.makedirs(folder__path)
	for key in Pawan__Share__Dictionary:
		Pawan__URL__Extract = Pawan__Share__Dictionary[key][0]
		Pawan__Number__of__Shares = Pawan__Share__Dictionary[key][1]
		Pawan__Invested__Amount = Pawan__Share__Dictionary[key][2]
		Pawan__Name = f"{folder__path}{key}.png"
		Pawan__Generate__Image(Pawan__URL__Extract, Pawan__Name)
	Pawan__Zoom__Images(folder__path)


def Pawan__Generate__Image(Pawan__URL__Extract, Pawan__Name):
	chrome_options = Options()
	chrome_options.add_argument("--headless=old")  # Runs Chrome in headless mode (no GUI)
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--log-level=3")  # Suppress most logs (INFO, WARNING, etc.)
	chrome_options.add_argument("window-size=1920x250")

	# Start Chrome browser with WebDriver Manager0
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

	# Open the given URL
	driver.get(Pawan__URL__Extract)

	# Add some delay to allow the page to load completely
	time.sleep(5)

	driver.execute_script("window.scrollBy(0, 260);")
	time.sleep(3)


	# Save the screenshot with the provided name
	screenshot = driver.get_screenshot_as_png()
	Pawan__Captured__Image = Image.open(io.BytesIO(screenshot))
	Pawan__Captured__Image = Pawan__Captured__Image.convert('L')
	enhancer = ImageEnhance.Contrast(Pawan__Captured__Image)
	Pawan__Captured__Image = enhancer.enhance(2.0)
	Pawan__Captured__Image.save(Pawan__Name)

	# Close the browser
	driver.quit()

def Pawan__Zoom__Images(folder__path):
	zoom_factor=1.4
	for filename in os.listdir(folder__path):
		if filename.endswith(".png"):
			image_path = os.path.join(folder__path, filename)
			img = Image.open(image_path)
			width, height = img.size
			new_width = int(width * zoom_factor)
			new_height = int(height * zoom_factor)
			zoomed_img = img.resize((new_width, new_height), Image.LANCZOS)  # LANCZOS for high-quality resizing
			zoomed_img.save(image_path)
			print(f"Zoomed {filename} to 140% and saved.")
			print("\n","\n")


if __name__ == '__main__':
	Pawan__Load__JSON()
	time.sleep(11)