from django.shortcuts import render
from .utils import length_converter, weight_converter, temperature_converter


def length(request):
    template = 'unit/length.html'
    get_length = request.GET.get('length')
    get_from_unit = request.GET.get('length-from')
    get_to_unit = request.GET.get('length-to')
    result = 0.0

    if get_length is not None and get_length != '':
        result = length_converter(value=int(get_length),
                                  from_unit=get_from_unit,
                                  to_unit=get_to_unit)

    context = {'result': result}

    return render(request, template, context)


def weight(request):
    template = 'unit/weight.html'
    get_weight = request.GET.get('weight')
    get_from_unit = request.GET.get('weight-from')
    get_to_unit = request.GET.get('weight-to')
    result = 0.0

    if get_weight is not None and get_weight != '':
        result = weight_converter(value=int(get_weight),
                                  from_unit=get_from_unit,
                                  to_unit=get_to_unit)

    context = {'result': result}
    return render(request, template, context)


def temperature(request):
    template = 'unit/temperature.html'
    get_temperature = request.GET.get('temperature')
    get_from_unit = request.GET.get('temperature-from')
    get_to_unit = request.GET.get('temperature-to')
    result = 0.0

    if get_temperature is not None and get_temperature != '':
        result = temperature_converter(value=int(get_temperature),
                                       from_unit=get_from_unit,
                                       to_unit=get_to_unit)

    context = {'result': result}
    return render(request, template, context)
