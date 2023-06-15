###############################################################
# Source Code originated from https://choiblog.tistory.com/55 #
###############################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os
import sys

# get arguments from command line
my_id = sys.argv[1]
my_pw = sys.argv[2]
shutdown_wait_time = sys.argv[3]

# Browser Options
options = Options()
options.add_argument('--incognito') #inprivate mode
# width of window size should be larger than certain value for access time_btn
options.add_argument('--window-size=1600,1080')
options.add_experimental_option('detach', True) # terminal chorme when process is terminated
options.add_experimental_option("excludeSwitches", ['enable-logging']) # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.get(r"https://flex.team/auth/login?nextUrl=%2Fhome")
driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.XPATH, \
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/div/div/form/div/label/div/div[1]/div[2]/div[2]/input")\
        .send_keys(my_id)
driver.find_element(By.XPATH, \
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/div/div/form/div/label/div/div[2]/button")\
        .click()
driver.find_element(By.XPATH, \
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/form/div/div[2]/label/div/div[1]/div[2]/div[2]/input")\
        .send_keys(my_pw)
driver.find_element(By.XPATH, r"/html/body/div[1]/main/div/div/div/article/div/div[2]/form/div/button[1]").click()
# site login
sleep(5)
time_btn = wait.until(\
    EC.element_to_be_clickable((By.XPATH, \
        r"/html/body/div[1]/div/div/div/nav/div/div[1]/div[2]/div/div/button")))
time_btn.click()
driver.find_element(By.XPATH, r"/html/body/div[6]/div/div/div/div/div/div[4]/div[2]").click()
confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, r"/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/div[2]/button[2]")))
confirm_btn.click()
sleep(max(2, int(shutdown_wait_time)))
os.system("shutdown now -f")