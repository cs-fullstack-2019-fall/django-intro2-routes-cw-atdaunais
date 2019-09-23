from django.http import HttpResponse


def goGetTheGood(request):
    return HttpResponse("Here you go! Final Fantasy 7 Remake!")


def happyHappyJoyJoy(request):
    return HttpResponse("My sister's getting married this week!")


def acceptString(request, text):
    return HttpResponse(text)