from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from data_scraping import *
from config import *

data_dict = {}
header = []
lines = []

driver = get_driver()
driver.get('http://e-negocioscidadesp.prefeitura.sp.gov.br/')

botao_licitacoes = driver.find_element_by_xpath('//*[@id="ctl00_cphConteudo_uccPainelLicitacao_lbtTotalLicitacoes"]')
botao_licitacoes.click()
sleep(5)

# Coleta informacao do header da tabela
for _ in range(5):
        header.append(driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[1]/th[{}]'.format(_ + 1)).get_attribute('abbr'))

botao_avancar = driver.find_element_by_css_selector('#ctl00_cphConteudo_gdvResultadoBusca_pgrGridView_btrNext_lbtText')

while botao_avancar:
        for _ in range(len(driver.find_element_by_xpath('//*[@id="ctl00_cphConteudo_gdvResultadoBusca_gdvContent"]').find_elements_by_tag_name('tr')) - 1):
                i = 1
                for key in header:
                        if key in data_dict.keys():
                                data_dict[key].append(driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[{}]/td[{}]'.format(_ + 2, i)).text)
                        else:
                                data_dict[key] = [driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[{}]/td[{}]'.format(_ + 2, i)).text]
                        i += 1
        
        try:
                driver.find_element_by_css_selector('#ctl00_cphConteudo_gdvResultadoBusca_pgrGridView_btrNext_lbtText').click()
        except Exception:
                break
        sleep(3)

print('stop')
