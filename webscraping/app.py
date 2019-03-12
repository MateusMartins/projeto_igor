from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from data_scraping import get_botao_avancar, get_driver, get_header, get_value
from config import *
import database
import mysql.connector as mariadb

def app():

    mariadb_connection = database.mariadb_connection()
    cursor = mariadb_connection.cursor()
    
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
    for i in range(len(data_dict['Licitador'])):
        cursor.execute("insert into licitacao (dt_abertura, licitador, modalidade, nr_publicacao, objeto) VALUES ('{}','{}','{}','{}','{}')".format(data_dict[header[0]][i], data_dict[header[1]][i], data_dict[header[2]][i], data_dict[header[3]][i], data_dict[header[4]][i]))
    mariadb_connection.commit()
    return data_dict

data_dict = app()
