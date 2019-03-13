from config import *
import re

def get_header(driver, header = []):
        for _ in range(5):
                header.append(driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[1]/th[{}]'.format(_ + 1)).get_attribute('abbr'))
        return header

def get_value(driver, header = [], data_dict = {}):
        data_dict = data_dict
        for _ in range(len(get_table(driver).find_elements_by_tag_name('tr')) - 1):
                i = 1
                for key in header:
                        if key in data_dict.keys():
                                data_dict[key].append(check_value(driver, driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[{}]/td[{}]'.format(_ + 2, i)).text))
                        else:
                                data_dict[key] = [check_value(driver, driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/div[5]/div/div[6]/table/tbody/tr[{}]/td[{}]'.format(_ + 2, i)).text)]
                        i += 1
        return data_dict

def get_botao_avancar(driver):
        return driver.find_element_by_css_selector('#ctl00_cphConteudo_gdvResultadoBusca_pgrGridView_btrNext_lbtText')

def get_table(driver):
        return driver.find_element_by_xpath('//*[@id="ctl00_cphConteudo_gdvResultadoBusca_gdvContent"]')

def check_value(driver, value):
        if re.findall('\'|\"', value):
                return re.sub('\'|\"', '-', value)
        else:
                return value
