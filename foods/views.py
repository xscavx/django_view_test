from django.http import HttpResponse


def foods(request) -> HttpResponse:
    return HttpResponse("My first view! HEYAA")
