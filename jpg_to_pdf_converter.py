from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
# sc-11drgl3-0 sc-1az4ycp-0 cVkIfg
driver.get('https://smallpdf.com/jpg-to-pdf')
time.sleep(10)
cookie_box = driver.find_elements(By.CSS_SELECTOR,'button.sc-11drgl3-0.sc-1az4ycp-0.cVkIfg')
cookie_box[1].click()

time.sleep(5)
upload_box = driver.find_element(By.ID,"__picker-input")
upload_box.send_keys("/Users/vijayvarma/Documents/Python Selenium/file.jpg")
print("Successfully Uploaded Data")
time.sleep(15)
convert_button = driver.find_elements(By.CSS_SELECTOR,'button.sc-11drgl3-0.sc-1az4ycp-0.cVkIfg')
print(convert_button)
convert_button[1].click()
print("Clicked the Convert Button")
time.sleep(20)
download_button = driver.find_elements(By.CSS_SELECTOR,'button.sc-11drgl3-0.sc-1az4ycp-0.cVkIfg')
print(download_button)
download_button[1].click()
print("Clickked DOwnlaod")
save_button = driver.find_element(By.CSS_SELECTOR,'a.lqkt1b-0.fdItuc.sc-1vytmrh-1.jaXOxZ')
save_button.click()
time.sleep(15)
driver.close()
#lqkt1b-0 fdItuc sc-1vytmrh-1 jaXOxZ
#driver.quit()