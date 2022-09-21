# import required modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://formsg-evaltest.as.r.appspot.com/responses")
driver.implicitly_wait(10)
results = driver.find_element(By.TAG_NAME, 'pre')

# Use BS to parse results
output = BeautifulSoup(results.get_attribute('innerText'), 'html.parser')
driver.implicitly_wait(10)
print(output)

# Output to html file
with open("test.txt", "a") as file:
    file.write(str(output))
