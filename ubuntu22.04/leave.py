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
wait_time = int(sys.argv[3])

# Browser Options
options = Options()
options.add_argument('--incognito') #inprivate mode
# width of window size should be larger than certain value for access time_btn
options.add_argument('--window-size=1600,1080')
options.add_experimental_option('detach', True) # terminal chrome when process is terminated
options.add_experimental_option("excludeSwitches", ['enable-logging']) # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.get(r"https://flex.team/auth/login?nextUrl=%2Fhome")

# ID
id_field = wait.until(EC.visibility_of_element_located((By.XPATH, \
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/div/div/form/div/label/div/div[1]/div[2]/div[2]/input")))
id_field.send_keys(my_id)

driver.find_element(By.XPATH, \
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/div/div/form/div/label/div/div[2]/button")\
        .click()
# PW
pw_field = wait.until(EC.visibility_of_element_located((By.XPATH,\
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/form/div/div[2]/label/div/div[1]/div[2]/div[2]/input")))
pw_field.send_keys(my_pw)
# sign in
driver.find_element(By.XPATH,\
    r"/html/body/div[1]/main/div/div/div/article/div/div[2]/form/div/button[1]")\
        .click()
# waiting for main page of flex
sleep(wait_time)
time_btn = driver.find_element(By.XPATH,\
    r"/html/body/div[1]/div/div/div/nav/div/div[1]/div[2]/div/button")
time_btn.click()

confirm_btn = wait.until(\
    EC.element_to_be_clickable((By.XPATH, \
        r"/html/body/div[7]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/button")))
confirm_btn.click()
end_now = wait.until(\
    EC.element_to_be_clickable((By.XPATH, \
        r"/html/body/div[8]/div/div/div/div/div/div[2]/div/div")))
end_now.click()
final_btn = wait.until(\
    EC.element_to_be_clickable((By.XPATH,\
        r"/html/body/div[7]/div/div/div/div/div/div/div/div/div/section/div/div[3]/button[2]")))
final_btn.click()
sleep(wait_time)
os.system("shutdown now -f")