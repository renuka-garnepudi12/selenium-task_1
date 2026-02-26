from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Browser
driver = webdriver.Chrome()

# Open Login Page
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Enter Username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter Password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click Login
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

time.sleep(2)

# Verify Login
message = driver.find_element(By.ID, "flash").text
print("Login Message:", message)

# Screenshot
driver.save_screenshot("login_success.png")

# Navigate to Home Page
driver.get("https://the-internet.herokuapp.com/")
print("Navigation Successful")

time.sleep(2)

# Close Browser
driver.quit()