from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Chrome(executable_path = r'C:\Users\Triton\Documents\chromedriver.exe')
driver.get("https://play.pokemonshowdown.com")
assert "Showdown" in driver.title
#try:
#    element = WebDriverWait(driver, 10).until(
#        EC.text_to_be_present_in_element_value((By.Name, "login"))
#    )
#finally:
driver.implicitly_wait(10)
loginBox = driver.find_element_by_name("login").click();
#elem = driver.find_element_by_id("email")
#elem.send_keys(user)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)
#driver.close()