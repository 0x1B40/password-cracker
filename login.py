from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

browser = webdriver.Chrome()
browser.get((''))

# fill in username and hit the next button

username = browser.find_element_by_id('')
username.send_keys(usernameStr)

#nextButton = browser.find_element_by_id('identifierNext')
#nextButton.click()

# wait for transition then continue to fill items

#password = WebDriverWait(browser, 10).until(
#    EC.presence_of_element_located((By.NAME, "password")))

password =browser.find_element_by_id('')

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('entry-login')
signInButton.click()

link = browser.find_element_by_id('')
link.click()

browser.get((''))
#WebDriverWait(browser, 5)


browser.get((''))
browser.get((''))



browser.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]').click()
browser.get((''))

password =browser.find_element_by_name('password')
now = datetime.now()
print("current time:",now)

for x in range(10000):
    password.send_keys(x)
    browser.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]').click()
    password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    print("tried:" ,x)
    
print("after entries:", datetime.now())





