from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email = "email"
password = "pass"
#email = "your_username"
#password = "your_password"
file_path = "/Users/vijayvarma/Documents/Python Selenium/file.pdf"

driver = webdriver.Chrome()
time.sleep(5)

driver.get('https://canvas.instructure.com/login/canvas')
time.sleep(5)

email_box = driver.find_element(By.ID,'pseudonym_session_unique_id')
password_box = driver.find_element(By.ID,'pseudonym_session_password')

email_box.send_keys(email)
password_box.send_keys(password)
time.sleep(1)
login_button = driver.find_element(By.CSS_SELECTOR,'button.Button.Button--login')
login_button.click()
time.sleep(5)

assignments_link = driver.find_element(By.CSS_SELECTOR,"a.ic-DashboardCard__action.assignments")
assignments_link.click()
time.sleep(5)

assignment_link = driver.find_element(By.CSS_SELECTOR,'a.ig-title')
assignment_link.click()
time.sleep(5)

start_assignment_link = driver.find_element(By.CSS_SELECTOR,'button.Button.Button--primary.submit_assignment_link')
start_assignment_link.click()
time.sleep(4)
file_upload = driver.find_element(By.CSS_SELECTOR,'input.input-file')
file_upload.send_keys(file_path)
time.sleep(2)
submit_button = driver.find_element(By.CSS_SELECTOR,'button#submit_file_button.btn.btn-primary')
submit_button.click()
time.sleep(10)
print("File is Successfully Submitted")
driver.close()