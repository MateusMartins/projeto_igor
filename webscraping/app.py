import sys
sys.path.insert(0, '/home/mateus/Área de Trabalho/trabalho/projeto_igor/')
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from webscraping.data_scraping import get_botao_avancar, get_header, get_value
from webscraping.config import get_driver
from webscraping.input import input_table

def app():
    
    data_dict = {}
    header = []

    driver = get_driver()
    driver.get('http://e-negocioscidadesp.prefeitura.sp.gov.br/')

    botao_licitacoes = driver.find_element_by_xpath('//*[@id="ctl00_cphConteudo_uccPainelLicitacao_lbtTotalLicitacoes"]')
    botao_licitacoes.click()
    sleep(5)

    header = get_header(driver, header)

    botao_avancar = get_botao_avancar(driver)

    while botao_avancar:
        data_dict = get_value(driver, header, data_dict)
        try:
            driver.find_element_by_css_selector('#ctl00_cphConteudo_gdvResultadoBusca_pgrGridView_btrNext_lbtText').click()
            sleep(3)
        except Exception:
            break
    
    sleep(3)
    
    return input_table(data_dict, header)

print(app())
