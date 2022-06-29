# Get data from 'https://data.korona.gov.sk/
import requests


base = 'https://data.korona.gov.sk/api'


# Ag testy
def ag_testy():
    json = requests.get(f'{base}/ag-tests/in-slovakia').json()
    result_dict = {
        'positives_count': str(json['page'][1]['positives_count']),
        'negatives_count': str(json['page'][1]['negatives_count']),
        'updated_at': str(json['page'][1]['updated_at'])
    }
    return result_dict


# Vaccinations
def vaccinations():
    json = requests.get(f'{base}/vaccinations/in-slovakia').json()
    result_dict = {
        'dose1_sum': str(json['page'][1]['dose1_count']),
        'dose2_sum': str(json['page'][1]['dose2_count']),
        'updated_at': str(json['page'][1]['updated_at'])
    }
    return result_dict
