from django.shortcuts import render


def length(request):
    template = 'unit/length.html'
    return render(request, template)


def weight(request):
    pass


def temperature(request):
    pass
