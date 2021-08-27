import zipfile
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=dane&dptoSeleccionado=&entidadSeleccionado=&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=0&max=10")

time.sleep(2)
nextpage = driver.find_element_by_xpath('//*[@id="div-resultados-busqueda"]/div[2]/ul[2]/li[14]/a')
nextpage.click()