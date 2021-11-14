
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# login with credentials
username = "testinggeek@tmpbox.net"
password = "123456789"
# login with no credentials
#username = ""
#password = ""

# initialize the Chrome driver
#driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()

# link to evernote login page
driver.get("https://www.evernote.com/Login.action")
# find username/email field and send the username itself to the input field
email=driver.find_element(By.TAG_NAME,"input#username.TextInput.TextInput_large")
email.send_keys(username)
email.send_keys(Keys.RETURN)
# find password input field and insert password as well
# wait for password field to appaer
driver.implicitly_wait(20) 
passW = driver.find_element(By.TAG_NAME,"input#password.TextInput.TextInput_large")
passW.send_keys(password)
passW.send_keys(Keys.RETURN)
# click login button
driver.find_element(By.TAG_NAME,"input#loginButton.Btn.Btn_emph.Btn_super").Click()
#logbutton.click()
'''
# waitting to be complete
#WebDriverWait(driver=driver, timeout=10).until(
#    lambda x: x.execute_script("return document.readyState === 'complete'")
#)'''

driver.implicitly_wait(300) 
driver.close()
