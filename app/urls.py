from django.urls import path, include
from .views import *


urlpatterns = [   
    #Start CustomerChat page paths =============================================
    path('Chat', CustomerChat_View, name='CustomerChat'),
    path('CustomerRequest_API', CustomerRequest_API, name='CustomerRequest_API'),
    
    #End CustomerChat page paths =============================================
    #Start translatorChat page paths =============================================
    path('TranslatorRequest_API', TranslatorRequest_API, name='TranslatorRequest_API'),
    #End translatorChat page paths =============================================

    path('cancel_appointment_API', cancel_appointment_API, name='cancel_appointment_API'),
    path('paid', paid, name='paid'),
    
    path('create_appointment', create_appointment, name='create_appointment'),#API--

]

