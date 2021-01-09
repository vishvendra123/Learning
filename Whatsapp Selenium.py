from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


name = input("Enter the name of person: ")
msg = input("Enter your message: ")
count = int(input("How many times you want to repeat the message: "))

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.set_page_load_timeout(10)
print("Scan QR code from your mobile.... wait time 30 sec")
time.sleep(30)
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

text_box = driver.find_element_by_class_name("DuUXI")
for i in range(count):
    text_box.send_keys(msg)
    time.sleep(1)
    send = driver.find_element_by_class_name("_2Ujuu")
    send.click()
    #text_box.send_keys(Keys.RETURN)
    time.sleep(1)



