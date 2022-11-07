
from selenium import webdriver

driver =  webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe") # executable_path=  driver root
driver.get("https://www.google.com") # Open a google page
driver.close() # Close the browser
