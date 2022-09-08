from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException as CLKERROR
from selenium.webdriver.support.select import Select
from time import sleep

url = 'https://citas.sre.gob.mx'
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=chrome_options)
driver.get(url)
driver.implicitly_wait(20)

my_email = 'khavari.7878@yahoo.com'
my_password = 'aA123456789@'
country_name = 'argentina'
first_name_is = "MOHAMMAD"
last_name_is = "KHAVARI"
yy_birth = 2000 
mm_birth = 1
dd_birth = 15

en_xpath = '//*[@id="subenlaces"]/ul[4]/a'
btn_consular_xpath = '/html/body/div[2]/div/main/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/button[2]'
#btn_mexico   = '/html/body/div[2]/div/main/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/button[1]'
email_xpath = '/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/div[2]/form/div[1]/div/input'
password_xpath = '/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/input'
btn_check_xpath = '/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/div[2]/form/div[4]/div/div/label/input'
btn_warning1_xpath = '//div[@class="modal-body"]/a/span/*[name()="svg"]'
btn_start_xpath = '//div[@class="row"]/div[2]'
btn_warning2_xpath = '//div[@class="form-group"]/a/span/*[name()="svg"]'
btn_schedule_xpath = '/html/body/div[2]/div[3]/div[3]/div[5]/a'
btn_warning3_xpath = '//div[@class="form-group"]/a/span/*[name()="svg"]'
country_xpath = '//*[@id="vs4__combobox"]/div[1]/input'
province_xpath = '//*[@id="vs2__combobox"]/div[1]/input'
office_xpath = '//*[@id="vs3__combobox"]/div[1]/input'
btn_select_xpath = "/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div/div/div[2]/div/center/a"
btn_accept_xpath = "/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/button[2]"
manually_xpath = "/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[4]/a"
first_name_xpath = "/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/form/div[1]/div[1]/div/input"
last_name_xpath = "/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/form/div[1]/div[2]/div/input"
select_year_xpath = '//*[@id="ui-datepicker-div"]/div/div/select[2]'
slecet_month_xpath = '//*[@id="ui-datepicker-div"]/div/div/select[1]'
date_input_xpath = '//input[@placeholder="YYYY-MM-DD"]'
# elem_table_xpath = '//*[@id="ui-datepicker-div"]/table'
day_xpath = '//td[@data-handler="selectDay"]/a'


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, en_xpath))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_consular_xpath))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, email_xpath))).send_keys(my_email)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(my_password)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_check_xpath))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_warning1_xpath))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_start_xpath))).click()
print("logged in")
WebDriverWait(driver,200).until(EC.url_matches("https://citas.sre.gob.mx/inbox"))
print("inbox ")
btn_warning2 = driver.find_element(By.XPATH , btn_warning2_xpath)
print("btn_warning 2 found")
sleep(.25)
try:
    btn_warning2.click()
    print("in first try")
except CLKERROR:
    sleep(.25)
    btn_warning2.click()
    print("in try again")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, btn_schedule_xpath))).click()
WebDriverWait(driver,200).until(EC.url_matches("https://citas.sre.gob.mx/appointment"))
print("appointment ")
sleep(4)
btn_warning3 = driver.find_element(By.XPATH , btn_warning3_xpath)
print("btn_warning 3 found")
btn_warning3.click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, country_xpath))).send_keys(country_name, Keys.ENTER)
print("country selected")
sleep(2)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, province_xpath))).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
print("city selected")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, office_xpath))).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
print("office slected")
sleep(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_select_xpath))).click()
print("office decieded")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btn_accept_xpath))).click()
print("accepted")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, manually_xpath))).click()
print("manually")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, first_name_xpath))).send_keys(first_name_is)
print("name typed")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, last_name_xpath))).send_keys(last_name_is)
print("last name typed")
driver.find_element(By.XPATH, date_input_xpath).click()
print("date open")
select_month = driver.find_element(By.XPATH, slecet_month_xpath)
print("month found")
select_month_object = Select(select_month)
select_month_object.select_by_index(str(mm_birth-1))
print("month selected")
select_year = driver.find_element(By.XPATH, select_year_xpath)
print("year found")
select_year_object = Select(select_year)
select_year_object.select_by_value(str(yy_birth))
print("year selected")
days = driver.find_elements(By.XPATH , day_xpath)
days[dd_birth - 1].click()    
print("date picked")