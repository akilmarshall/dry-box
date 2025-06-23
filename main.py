from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

from math import exp, pi


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

template_loader = FileSystemLoader(searchpath='template')
env = Environment(loader=template_loader)


@app.get('/', response_class=HTMLResponse)
def index():
    template = env.get_template('index.html')

    return template.render()


@app.get('/water-volume-mass', response_class=HTMLResponse)
def water_volume_mass(temperature: float, humidity: float):
    '''Given temperature and humidity computer the amount of water vapour in 1m3. '''
    # https://calculattor.com/volume-of-water-in-air-at-given-humidity-calculator/
    saturation_vp = 610.94 * exp((17.625 * temperature) / (temperature + 243.04))
    actual_vp = (humidity / 100) * saturation_vp
    absolute_hum = (actual_vp * 2.16679) / (temperature + 273.15)
    mass = absolute_hum * 1 # volume 1m3
    volume = mass / 1000

    template = env.get_template('water-volume-mass.html')

    return template.render(mass=mass, volume=volume)


@app.get('/filament-mass', response_class=HTMLResponse)
def filament_mass(length: float, material: str):

    template = env.get_template('filament-mass.html')

    match material:
        case 'PLA':
            density = 1.24  # g/cm3
        case 'PETG':
            density = 1.27  # g/cm3
        case _:
            density = 0  # all others are undefined

    r = 0.175 / 2
    volume = length * pi * r ** 2

    mass = volume * density

    return template.render(mass=mass)


@app.get('/filament-water', response_class=HTMLResponse)
def water_content_in_filament(ideal: float, actual: float):
    template = env.get_template('filament-water.html')

    percent = (actual / ideal) - 1

    sample = (actual - ideal) * 1000
    whole = 1000 * percent

    return template.render(percent=100 * percent, sample=sample, whole=whole)
