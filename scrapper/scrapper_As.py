import requests
from django.utils.text import slugify
from bs4 import BeautifulSoup
from .models import diario_as


class ScrapperAS():
    def __init__(self):
        self.url ="https://colombia.as.com/resultados/futbol/primera/clasificacion/"
        self.html = None
        self.data = []

    def get_html(self):
        if not self.html:
            response = requests.get(self.url)
            self.html = response.text
        return self.html

    def parser_html(self, html):
        self.soup = BeautifulSoup(self.html, 'html.parser')
        tbody_list = self.soup.select('tbody tr')

        nombre_equipo = list()
        points = list()

    

        for row in range(20):
            nombre = tbody_list[row].find('span', {'class': 'nombre-equipo'}).getText()
            point = tbody_list[row].find('td', {'class': 'destacado'}).getText()
            nombre_equipo.append(nombre)
            points.append(point)

        print((nombre_equipo))
        print((points))

        for rows in range(len(nombre_equipo)):
            diario_model = diario_as()
            diario_model.name = nombre_equipo[rows]
            diario_model.point = points[rows]
            diario_model.save()



    def run(self):
        self.get_html()
        self.parser_html(self.html)
