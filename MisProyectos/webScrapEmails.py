import urllib.request
from bs4 import BeautifulSoup

url = "https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=dane&dptoSeleccionado=&entidadSeleccionado=&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=50&max=10"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,"html.parser")

clientes = soup.find_all("a", {"class": "https://www.funcionpublica.gov.co/web/sigep/hdv/-/directorio/M82896-0020-4/view"})

for elem in clientes:
    titulo = elem.find("td",{"class":"columna-datos"})
    email = elem.find_all("span")
    
    print(titulo,email)

    

