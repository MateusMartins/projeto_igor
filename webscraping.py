from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep

data_dict = {}
header = []
lines = []

driver = webdriver.Firefox()

driver.get('http://e-negocioscidadesp.prefeitura.sp.gov.br/')

sleep(5)

botao = driver.find_element_by_xpath('//*[@id="ctl00_cphConteudo_uccPainelLicitacao_lbtTotalLicitacoes"]')

botao.click()

# Coleta informacao do header da tabela
for _ in range(5):
    header.append(driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[1]/th[{}]'.format(_ + 1)).get_attribute('abbr'))

# Criacao do dicionario
for name in header:
    data_dict[name] = name

for _ in range(20):
    i = 1
    for key in data_dict:
        data_dict[key] = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[{}]/td[{}]'.format(_ + 2, i)).text
        i += 1
print('stop')

