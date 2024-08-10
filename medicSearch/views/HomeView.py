from django.http import HttpResponse


def home_view(reques):
    return HttpResponse('<h1>Olá mundo!</h1>', status=200)