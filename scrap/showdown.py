from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

user = "Automon"
pwd = "password"

driver = webdriver.Chrome(executable_path = r'C:\Users\Triton\Documents\chromedriver.exe')
driver.get("https://play.pokemonshowdown.com")
assert "Showdown" in driver.title

#Choosing Name Button Clicker
choosename_submit = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "login"))
)
choosename_submit.click()

#Username Autofill and Submit
username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

username_input.send_keys(user)
username_submit = driver.find_element_by_xpath("//form/p[@class='buttonbar']/button[1]")
username_submit.send_keys(Keys.ENTER)

#Password Autofill and Submit
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password_input.send_keys(pwd)
password_submit = driver.find_element_by_xpath("//form/p[@class='buttonbar'][1]/button[1]")
password_submit.send_keys(Keys.ENTER)


# driver.close()
