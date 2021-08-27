#-*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = 'https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=dane&dptoSeleccionado=&entidadSeleccionado=&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=40&max=10'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
#datos = page_soup.findAll("div",{"class":"div-resultados"})

datos1 = page_soup.findAll("td",{"class":"columna-datos"})

#print(datos1)
# print(datos)

for elem in datos1:
    titulo = elem.find("td",{"class":"columna-datos"})
    email = elem.find_all("span")
    print(email)



with open("data1.txt", "w+") as f:
    for dato in email:
        str_value = str(dato)
        f.write(str_value)
        f.write("\n")

