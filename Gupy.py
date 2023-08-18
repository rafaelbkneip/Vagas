from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--start-maximized")
service = Service(executable_path="chromedriver")
navegador = webdriver.Chrome(options = options, service = service)

navegador.get("https://apogeu.gupy.io/")
driver=navegador
lista_qrcode = []
lista_vagas = []


for i in range(1,10):
    try:
        lista_qrcode.append(driver.find_element(By.XPATH, '//*[@id="job-listing"]/ul/li['+str(i)+']/a').get_attribute('href'))
        lista_vagas.append(driver.find_element(By.XPATH, '//*[@id="job-listing"]/ul/li['+str(i)+']/a/div/div[1]').text)

    except:
        print ("Não existe essa vaga")

sleep(5)
driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]').click()


sleep(10)
driver.find_element(By.XPATH, '//*[@id="job-listing"]/div[2]/nav/ul/li[4]/button').click()


for i in range(1,10):
    try:
        lista_qrcode.append(driver.find_element(By.XPATH, '//*[@id="job-listing"]/ul/li['+str(i)+']/a').get_attribute('href'))
        lista_vagas.append(driver.find_element(By.XPATH, '//*[@id="job-listing"]/ul/li['+str(i)+']/a/div/div[1]').text)
    except:
        print ("Não existe essa vaga")

print(lista_qrcode)
print(lista_vagas)