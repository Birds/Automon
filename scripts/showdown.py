from selenium import webdriver
from selenium.common.exceptions import WebDriverException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

user = "Automon"
pwd = "password"
default_timeout = 10
team_stream = """
Donphan @ Fairium Z  
Ability: Sturdy  
EVs: 248 HP / 140 Atk / 120 Def  
Relaxed Nature  
IVs: 17 Spe  
- Play Rough  
- Earthquake  
- Ice Shard  
- Counter  

Serperior @ Leftovers  
Ability: Contrary  
EVs: 244 HP / 8 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Leech Seed  
- Substitute  
- Protect  
- Leaf Storm  

Tyranitar @ Tyranitarite  
Ability: Sand Stream  
EVs: 136 HP / 124 Atk / 84 SpD / 164 Spe  
Adamant Nature  
- Rock Tomb  
- Taunt  
- Crunch  
- Fire Punch  
"""


def add_team_if_missing(team_string):
    """Return the pathname of the KOS root directory."""
    teambuilder_button = WebDriverWait(driver, default_timeout).until(
        EC.presence_of_element_located((By.NAME, 'joinRoom'))
    )
    teambuilder_button.send_keys(Keys.ENTER)  # enter teambuilder menu

    # check if team already exists
    try:
        exists = driver.find_element_by_xpath(
            "//div[@class='mainmenuwrapper']/div[@class='leftmenu']/div[@class='mainmenu']/div[@class='menugroup'][2]/p[1]/button[@class='button mainmenu2']").click()
    except ElementNotInteractableException:  # need to create team
        new_team_button = driver.find_element_by_name("newTop").click()
        import_from_text_button = driver.find_element_by_name("import").click()
        title_box_area = driver.find_element_by_class_name("textbox")
        for i in range(0, len("Untitled 1")):
            title_box_area.send_keys(Keys.BACK_SPACE)
        title_box_area.send_keys("teamname")
        text_box_area = driver.find_element_by_xpath(
        "//div[@id='room-teambuilder']/div[@class='teamwrapper']/div[@class='teamedit']/textarea[@class='textbox']").send_keys(
        team_stream)
        save_import_button = driver.find_element_by_name("saveImport").click()
        
        
def select_format():
    driver.get_element_by_name("format").click()
    driver.get_element_by_xpath("//div[@class='ps-popup']/ul[@class='popupmenu'][1]/li[14]/button").click()
    
def start_game():
    select_format()
    driver.get_element_by_name("team").click()
    driver.get_element_by_xpath("//div[@class='ps-popup']/ul[@class='popupmenu']/li[5]/button[@class='button']").click()
    driver.get_element_by_name("search").click()

try:
    driver = webdriver.Chrome(executable_path=r'C:\Users\leozh\Downloads\chromedriver.exe')
except WebDriverException:
    driver = webdriver.Chrome(executable_path=r'C:\Users\Triton\Documents\chromedriver.exe')

driver.get("https://play.pokemonshowdown.com")
assert "Showdown" in driver.title

# Choosing Name Button Clicker
choosename_submit = WebDriverWait(driver, default_timeout).until(
    EC.presence_of_element_located((By.NAME, "login"))
)
choosename_submit.click()

# Username Autofill and Submit
username_input = WebDriverWait(driver, default_timeout).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

username_input.send_keys(user)
username_submit = driver.find_element_by_xpath("//form/p[@class='buttonbar']/button[1]")
username_submit.send_keys(Keys.ENTER)

# Password Autofill and Submit
password_input = WebDriverWait(driver, default_timeout).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password_input.send_keys(pwd)
password_submit = driver.find_element_by_xpath("//form/p[@class='buttonbar'][1]/button[1]")
password_submit.send_keys(Keys.ENTER)



add_team_if_missing(team_stream)

start_game()
