#In this project the selenium is used to
#automate the form filling and submission process   

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element(By.NAME,'fName')
first_name.send_keys("Tushar")
last_name=driver.find_element(By.NAME,'lName')
last_name.send_keys("Pal")
mail=driver.find_element(By.NAME,'email')
mail.send_keys("rmppc@ambicasteels.com")

btn=driver.find_element(By.CSS_SELECTOR,"form button")

btn.click()
