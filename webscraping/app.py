from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from data_scraping import get_botao_avancar, get_driver, get_header, get_value
from config import *

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
    return data_dict

data_dict = app()
