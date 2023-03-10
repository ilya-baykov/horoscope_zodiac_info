import math

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
zodiac_dict = {

    (1, 'aries'): 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    (2, 'taurus'): 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    (3, 'gemini'): 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    (4, 'cancer'): 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    (5, 'leo'): 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    (6, 'virgo'): 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    (7, 'libra'): 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    (8, 'scorpio'): 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    (9, 'sagittarius'): 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    (10, 'capricorn'): 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    (11, 'aquarius'): 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    (12, 'pisces'): 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def zodiak_searcher(request, zodiac):
    for key in zodiac_dict:
        if zodiac in key:
            return HttpResponse(zodiac_dict[key])
    return HttpResponseNotFound(f"{zodiac} -Мы не знаем такого знака зодиака (((((")


def area_rectangle(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width} x {height} равна {width * height}")


def area_square(request, width):
    return HttpResponse(f"Площадь квадрата размером {width} x {width} равна {width * width}")


def area_circle(request, radius):
    return HttpResponse(f"Площадь круга с радиусом {radius} равна  {math.pi * math.pow(radius, 2)}")
