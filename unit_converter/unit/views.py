from django.shortcuts import render


def length(request):
    template = 'unit/length.html'   
    get_length = request.GET.get('length')

    if get_length:
        result = get_length
    else:
        result = 0.0

    context = {'result': result}

    return render(request, template, context)


def weight(request):
    template = 'unit/weight.html'
    get_weight = request.GET.get('weight')

    if get_weight:
        result = get_weight
    else:
        result = 0.0

    context = {'result': result}
    return render(request, template, context)


def temperature(request):
    template = 'unit/temperature.html'
    get_temperature = request.GET.get('temperature')

    if get_temperature:
        result = get_temperature
    else:
        result = 0.0

    context = {'result': result}
    return render(request, template, context)
