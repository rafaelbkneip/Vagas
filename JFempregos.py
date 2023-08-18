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

navegador.get("https://www.jfempregos.com.br/empresa/curso-apogeu-de-juiz-de-fora")

lista_jfempregos = []
lista_jfempregos_link = []

for i in range(10):
    try:                                                           
        lista_jfempregos.append(navegador.find_element(By.XPATH, '//*[@id="principal"]/section[1]/div/div[' + str(int(2*i -1))+']/div/div/a/table/tbody/tr/td[1]/h3').text)
        lista_jfempregos_link.append(navegador.find_element(By.XPATH, '//*[@id="principal"]/section[1]/div/div['+ str(int(2*i -1)) +']/div/div/a').get_attribute('href'))

    except:
        print("Não existe essa vaga")

print(lista_jfempregos)
print(lista_jfempregos_link)