from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import getpass

URL = 'https://gateway.iitk.ac.in:1003/login?'
USERNAME = 'suvambasak22'
PASSWORD = getpass.getpass(prompt='Password: ')

# Creating virtual display.
display = Display(visible=0, size=(1024, 768))
display.start()
print ('Creating virtual display...')

opts = webdriver.ChromeOptions()
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-setuid-sandbox')

# Web driver.
browser = webdriver.Chrome(options=opts)
print ('Configuring webdriver...')

# URL
browser.get(URL)
print ('URL: '+URL)

# username
username_textbox = browser.find_element(by=By.ID, value="ft_un")
username_textbox.send_keys(USERNAME)
print ('Setting username...')

# password
password_textbox = browser.find_element(by=By.ID, value="ft_pd")
password_textbox.send_keys(PASSWORD)
print ('Setting password...')

# Click sign in button.
link = browser.find_element(by=By.CLASS_NAME, value='primary')
print ('Signing in...')
link.click()

# Close display.
display.stop()
print ('Complete.')
