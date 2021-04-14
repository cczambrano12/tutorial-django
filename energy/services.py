from .models import Energy_generation
import requests
import logging
import math

# Get an instance of a logger
logger = logging.getLogger(__name__)

def get_irradiance(latitude, longitude):
    api_key = '98zmhw9ZK3qYRnZOch1SJhKoqfoXHAkHGvj1bxWx'
    params = {'api_key': api_key, 'lat': latitude, 'lon':longitude}
    api_url = 'https://developer.nrel.gov/api/solar/solar_resource/v1.json'
    response = requests.get(api_url, params=params)
    return response.json()

def get_nested_values(data, key):
    outputs = data.get('outputs', {})
    if (outputs and outputs != 'no data'):
        avg_dni = outputs.get('avg_dni', {})
        if (avg_dni and avg_dni != 'no data'):
            return avg_dni.get(key, 'no data')
    return 'no data'


def get_energy(latitude, longitude, tilt, power):
    energy_data = {}
    rated_kw_power = float(power)
    tilt_float = float(tilt)

    if(latitude != 0 and longitude != 0 ):
        irradiance_data = get_irradiance(latitude, longitude)
        # logger.warning(irradiance_data)
        irradiance_month = get_nested_values(irradiance_data,'monthly')
        energy_data['energy'] = {k: round(v*rated_kw_power * math.cos(tilt_float),2) for k, v in irradiance_month.items()} if(irradiance_month != 'no data') else 0

        irradiance_annual = get_nested_values(irradiance_data,'annual')
        energy_data['average_energy'] = round(irradiance_annual * rated_kw_power * math.cos(tilt_float),2) if(irradiance_annual != 'no data') else 0

        energy_data['year'] = 2021
        energy_data['power'] = rated_kw_power
        energy_data['latitude'] = latitude
        energy_data['longitude'] = longitude
        energy_data['tilt'] = tilt
        logger.warning(energy_data)

    return energy_data
