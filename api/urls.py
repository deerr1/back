
from django.contrib import admin
from django.urls import path, include

from Institutions import views as InstView

urlpatterns = [
    
    path('infoinstitutions/', InstView.InfoInstitutions.as_view() ),
]