import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerSignUpForm,AdminSignUpForm, TranslatorSignUpForm, LoginForm
from .models import Customer, Appointment, User, Translatorr
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TranslationRequest
from django.contrib.auth.hashers import make_password

#====================================================================================================
#Start CHAT PAGE View
#====================================================================================================
def CustomerChat_View(request):
    return render(request,'Pages/CustomerChat.html')


#API--------- FOR REPRESENT THE REQUESTS FOR THE CUSTOMER
@api_view(['POST','GET'])
def CustomerRequest_API(request):
    if request.method == 'POST':
        cutomerUsername = request.data.get("username")
        try:
           customerInfo = User.objects.get(username=cutomerUsername)
           customerid=customerInfo.id
           print('\n\n\n customerid:',customerid)
        except:
            return Response({"message": "there is no Customer with this username"})
        try:    
            appointments = Appointment.objects.filter(customerID=customerid)
            print('\n\n\n appointments:',appointments)
            
        except:
            return Response({"message": "There is no appointment yet"})
        
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    return Response({"message": "Welcome to the customer home page. Please enter your username."})



@api_view(['POST','GET'])
def TranslatorRequest_API(request):
    if request.method == 'POST':
        cutomerUsername = request.data.get("username")
        try:
           translatorInfo = User.objects.get(username=cutomerUsername)
           translatorId=translatorInfo.id
        except:
            return Response({"message": "there is no Customer with this username"})
        try:    
            appointments = Appointment.objects.filter(translatorId=translatorId)
            print('\n\n\n appointments:',appointments)
            
        except:
            return Response({"message": "There is no appointment yet"})
        
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    return Response({"message": "Welcome to the customer home page. Please enter your username."})

#====================================================================================================
#End CHAT PAGE View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Start Home Pages View
#====================================================================================================
#***************************The has same functiond put the go to deffrent Html **********************
def CustomerHomePage_View(request):    
    c= request.user
    cId=c.id
    if request.method == 'POST':
        Second_Language = request.POST.get('textfield', None)
        try:
            pro=Translatorr.objects.filter(Second_Language=Second_Language)
            appointment= Appointment.objects.filter(customerID=cId)
            x={'pro': pro, 'appointment':appointment}  
            return render(request,'Homes/representationOfTranslators.html', x)#for show the customer Home page                         
        except Translatorr.DoesNotExist :
            return HttpResponse("no such user")
    else:
        return render(request, 'Homes/customeHomePage.html')
   
#chose language API--------------------- 
@api_view(['GET', 'POST'])
def CustomerHomePage_API(request):
    if request.method == 'POST':
        Second_Language = request.data.get("Second_Language") # get user input language.
        print("\n\n\n  Language: ", Second_Language)
        t = Translatorr.objects.filter(Second_Language=Second_Language)     
        print("\n\n\n  t: ", t)    
        serializer = TranslatorSerializer(t, many=True)
        print("\n\n\n  serializer.data: ", serializer.data)
        return Response(serializer.data)
    else:
        return Response({"message": "Welcome to the customer home page. Please enter your preferred language Second_Language"})
    
#====================================================================================================
#End Customer Home Page
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
#Send request API------------------------------------------   
# @login_required  
@api_view(['POST','GET'])
def create_appointment(request):
    if request.method == 'POST':
        id = request.data.get("translatorId")
        cutomerUsername = request.data.get("cutomerUsername")
        try:
            print('\n\n\n cutomerUsername:', cutomerUsername)
            translator = Translatorr.objects.get(user_id=id)
            translatorName= translator.name #get the name of the translator
            translatorID= translator.user_id
            trnslator_Secound_language=translator.Second_Language
            #get the id of the translator
        except:
              return Response({"message": "there is no Translator with this id"})

        try:
           customer = User.objects.get(username=cutomerUsername)
           current_userId = customer.id
           customer = Customer.objects.get(user_id=current_userId)
           customerName=customer.name
           customer_First_language=customer.First_Language
        except:
              return Response({"message": "there is no Customer with this username"})

        appointment = Appointment.objects.create(customerName=customerName,translatorName = translatorName, 
            customerID=current_userId, translatorID=translatorID,  
            accepted=False, toLanguage=trnslator_Secound_language,
            fromLanguage=customer_First_language)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    return Response({"message": "Welcome to the customer home page. Please enter your preferred language."})
#====================================================================================================
#End Send request View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''
#====================================================================================================
#Start Accept/Reject translation
#====================================================================================================
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment  

@api_view(['POST','GET'])
def cancel_appointment_API(request): 
    if request.method == 'POST':
        id = request.data.get("appointmentID")
        appointment = get_object_or_404(Appointment, pk=id) 
        appointment.delete()  # Use delete() method to delete the appointment
        return Response({"message": "Appointment deleted successfully."}) 
    
    return Response({"message": "Enter Appointment ID for deletion: appointmentID "}) 


@api_view(['POST','GET'])
def paid(request): 
    if request.method == 'POST':
        id = request.data.get("appointmentID")
        appointment = get_object_or_404(Appointment, pk=id) 
        appointment.paid=True
        appointment.paidTime=datetime.datetime.now()
        appointment.save()  
        serializer=AppointmentSerializer(appointment)
        return Response(serializer.data) 
    return Response({"message": "Enter Appointment ID for pay to the appointment: appointmentID "}) 


#====================================================================================================
#End Accept/Reject translation
#====================================================================================================

'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''

#====================================================================================================
#Start Translator Home page  
#====================================================================================================

#====================================================================================================
#Start payment  
#======
