from .models import Elector, VotantesPorProvincia, VotantesPorCanton , VotantesPorDistrito, DistritoElectoral
from django.db.models import Q, Count
import threading
import time


class Statistics:

    def __init__(self):
        self.threads = list()
        self.province_statistics = {}
        self.canton_statistics = {}
        self.district_statistics = {}
        self.identification_statistics = {}
        self.statistics_names = [
            'total_votantes',
            'total_votantes_hombres',
            'total_votantes_mujeres'
        ]

    def get_polling_statistics(self, expiration_date, province, canton, district):
        self.province_statistics = VotantesPorProvincia.objects.filter(provincia=province).values(*self.statistics_names)
        self.canton_statistics = VotantesPorCanton.objects.filter(codigo_provincia__provincia=province, canton=canton).values(*self.statistics_names)
        self.district_statistics = VotantesPorDistrito.objects.filter(distrito = district, codigo_canton__canton=canton , codigo_canton__codigo_provincia__provincia=province).values(*self.statistics_names)
        self.identification_statistics = {'same_id_count': Elector.objects.filter(fecha_caducidad=expiration_date).count()}

     
        return {'province_statistics': self.province_statistics[0],
                'canton_statistics': self.canton_statistics[0],
                'district_statistics': self.district_statistics[0],
                'id_statistics': self.identification_statistics}

