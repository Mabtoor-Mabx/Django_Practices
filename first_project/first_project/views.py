from django.http import HttpResponse
from django.shortcuts import render
import datetime

# # A simple Function View Based

# # def home(request):
# #     return HttpResponse("Hello! This is My First Django App")
# # def About(request):
# #     return HttpResponse("Hello ! This is About Us Page")
# # def contact(request):
# #     return HttpResponse("Hello! This is Contact Us Page")
# # def services(request):
# #     return HttpResponse("Hello! This Is Services Based Page")

# def home(request):
#     context = {
#         'message': 'Hello! This is Message Getting from Views.py file inside HTML Tag'
#     }
#     return render(request, 'index.html', context)


def home(request):
    context = {
        'user_name': 'Mabtoor',
        'is_logged_in': True,
        'Favouite_food': ['Biryani', 'Pizza', 'Burgers', 'Pasta', 'Fried Rice'],
        'year': datetime.datetime.now().year
    }

    return render(request, 'home.html', context)