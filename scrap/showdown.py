from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

user = "Automon"
pwd = "password"

driver = webdriver.Chrome(executable_path=r'C:\Users\leozh\Downloads\chromedriver.exe')
driver.get("https://play.pokemonshowdown.com")
assert "Showdown" in driver.title
# try:
#    element = WebDriverWait(driver, 10).until(
#        EC.text_to_be_present_in_element_value((By.Name, "login"))
#    )
# finally:

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "login"))
)

element.click()

choose_name_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

choose_name_element.send_keys(user)
# element.send_keys(Keys.ENTER)


# driver.implicitly_wait(10) #old
# loginBox = driver.find_element_by_name("login").click()
# elem = driver.find_element_by_id("email")
# elem.send_keys(user)
# elem = driver.find_element_by_id("pass")
# elem.send_keys(pwd)
# elem.send_keys(Keys.RETURN)
# driver.close()
