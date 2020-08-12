from .models import Elector, DistritoElectoral, VotantesPorProvincia, VotantesPorCanton
from django.db.models import Q, Count
import threading


class Queries:

    def __init__(self, elector_id="", elector_name="", elector_first_surname="", elector_second_surname="", elector_option=""):
        self.elector_identification = elector_id
        self.elector_name = elector_name.upper()
        self.elector_first_surname = elector_first_surname.upper()
        self.elector_second_surname = elector_second_surname.upper()
        self.elector_option = elector_option

    # Returns the information by searching according to the option that the user chose
    def search_polling_information(self):
        values = ['nombre', 'primer_apellido', 'segundo_apellido', 'cedula', 'codigo_electoral__provincia',
                  'codigo_electoral__canton', 'codigo_electoral__distrito', 'codigo_electoral', 'fecha_caducidad']

        if(self.elector_option == '1'):  # Search by name
            result = Elector.objects.filter(nombre=self.elector_name,
                                            primer_apellido=self.elector_first_surname,
                                            segundo_apellido=self.elector_second_surname).values(*values)

        elif self.elector_option == '2':  # Search by identification
            result = Elector.objects.filter(cedula=self.elector_identification).values(*values)

        if len(result) > 0:
            result = result[0]

        else: 
            result = []

        return result
