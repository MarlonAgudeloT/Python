# ESTE SI ESTA FUNCIONANDO
#-*- coding: utf-8 -*-
import os
import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


#Aqui ingresamos a la pagina que deseamos scrapear

driver = webdriver.Chrome(ChromeDriverManager().install()) # ESTO SIRVE PARA ABRIR LA PAGINA DESDE EL IDE
driver.get("https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=pereira&dptoSeleccionado=&entidadSeleccionado=0445&munSeleccionado=PEREIRA&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=")

url = 'https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=pereira&dptoSeleccionado=&entidadSeleccionado=0445&munSeleccionado=PEREIRA&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado='
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser") # Esto modifica el formato html para convertirlo en datos que puede leer Python
time.sleep(5)

#BUSCANDO LOS LINKS PARA PASAR LAS PAGINAS
"""allLinks = []
links = [a.attrs.get('href') for a in page_soup.select('a[href]') ]
for i in links:
    if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
        allLinks.append(i)

print("Links "+allLinks)"""

#AQUI BUSCAMOS LOS DATOS QUE NOS INTERESAN
datos1 = page_soup.findAll("span")

emails = []
def findMails(datos1):
    for name in datos1:
        TextMail = name.text
        #name=re.findall(TextMail,'[a-zA-Z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,}') #Esta es otra forma de buscar el email
        name=re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',TextMail)#Esta liena de codigo nos permite buscar el email
        #Con este If limpiamos los datos para que queden guardados de una forma mas ordenada
        if('@' in TextMail):
            TextMail=TextMail.replace(" ",'').replace('\r','')
            TextMail=TextMail.replace('\n','').replace('\t','')
            if(len(emails)==0)or(TextMail not in emails):
                #print(TextMail)
                emails.append(TextMail)
print("Aqui")
findMails(datos1) # EJECUTAMOS LA FUNCION PARA QUE BUSQUE Y AGREGUE LOS DATOS A LA LISTA VACIA

#ESTA ES OTRA FORMA DE CREAR Y ESCRIBIR EN UN ARCHIVO, PERO COMO ESTAMOS USANDO PANDAS ES MAS FACIL
"""with open("data1.txt", "w+") as f:
    for dato in emails:
        str_value = str(dato)
        f.write(str_value)
        f.write("\n")  
        print(dato)"""

#ESTO SE HACE CON PANDAS Y MANEJO DE DATAFRAMES
#PARA GUARDAR EN UN ARCHIVO CSV

patron = r'[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+.[a-z]{2,}'

coincidencia = re.findall(patron,emails)
print(coincidencia)

df = pd.DataFrame({"elementos":coincidencia})

df.to_csv('emails.csv',mode = 'a', index = False, header = False)

print(df)


#ESTE CODIGO NOS SIRVE PARA PASAR LAS PAGINAS

time.sleep(2)
nextpage = driver.find_element_by_xpath('//*[@id="div-resultados-busqueda"]/div[2]/ul[2]/li[14]/a')
nextpage.click()
