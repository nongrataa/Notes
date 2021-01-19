from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),

    path('<int:note_id>/', detail, name='detail'),

    path('<int:question_id>/results/', results, name='results'),

    path('<int:question_id>/vote/', vote, name='vote'),
]