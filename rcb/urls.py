from django.urls import path
from rcb.views import *
app_name = 'anything'
urlpatterns = [
     path('king/',king, name='king'),
]

