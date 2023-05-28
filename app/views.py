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
#Star log in view
#====================================================================================================
def login_view(request):
    model=User
    template_name='login.html'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            formm = LoginForm(request.POST or None)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('customer_Home_Page')
            elif user is not None and user.is_translator:
                login(request, user)
                return redirect('translator_Home_Page')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    else:
        form = AuthenticationForm()
    return render(request, 'logIn/login.html', {'form': form})


#api--------------------------------------------------------------------------------
@api_view(['POST', 'GET'])
def login_view2(request):
    serializer = LoginFormSerializer(data=request.data)
    print('\n\n\n', serializer )
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        print('\n\n\n username and ',username,password)
        user2 = authenticate(username=username, password=password)
        print('\n\n\nuser:', user2)
        if user2 is not None and user2.is_customer:
            print("\n\n\n is_customer")
            login(request, user2)
            return Response(UserSerializer(user2).data)
        elif user2 is not None and user2.is_translator:
            print("\n\n\n is_translator")
            login(request, user2)
            return Response(UserSerializer(user2).data)
        elif user2 is not None and user2.is_Admin:
            print("\n\n\n is_Admin")
            login(request, user2)
            return Response(UserSerializer(user2).data)

        else:
            print('\n\n\n not1\n\n\n')
            return Response({'error': True})
    else:
        print('\n\n\n not \n\n\n')
        return Response(serializer.errors, status=400)
    
    
@api_view(['POST'])
def check_username(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'is_available': False})
        else:
            return Response({'is_available': True})
    else:
        return Response({'error': True})

#====================================================================================================
#End log in view
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#Star home page View
#====================================================================================================
def home(request):
    return render(request,'home.html')#for show the log in or sign up choice page 
#====================================================================================================
#End home page View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Start signUp View
#====================================================================================================

def index(request):
    return render(request,'signUpPage.html')

#====================================================================================================
#End signUp View
#====================================================================================================
'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#====================================================================================================
#Start Profile View
#====================================================================================================

@api_view(['POST','GET'])
def CustomerProfile_API(request):
    if request.method == 'POST':
        cutomerUsername = request.data.get("username")
        try:
           UserInfo = User.objects.get(username=cutomerUsername)
           userID=UserInfo.id
           customerInfo = Customer.objects.get(user_id=userID)
        except:
            return Response({"message": "there is no Customer with this username"})
        
        serializer=UserSerializer(UserInfo)
        serializerCustomer=CustomerSerializer(customerInfo)
        data = {
                "user": serializer.data,
                "customer": serializerCustomer.data
            }
        return Response(data)
    return Response({"message": "Welcome to the customer Profile page. Please enter your username."})

#ٌtranslatoor------------------------------------------
@api_view(['POST','GET'])
def translatorProfile_API(request):
    if request.method == 'POST':
        cutomerUsername = request.data.get("username")
        try:
           UserInfo = User.objects.get(username=cutomerUsername)
           userID=UserInfo.id
           customerInfo = Translatorr.objects.get(user_id=userID)
        except:
            return Response({"message": "there is no Customer with this username"})
        
        serializer=UserSerializer(UserInfo)
        serializerCustomer=TranslatorSerializer(customerInfo)
        data = {
                "user": serializer.data,
                "translator": serializerCustomer.data
            }
        return Response(data)

    return Response({"message": "Welcome to the customer Profile page. Please enter your username."})
#====================================================================================================
#End Profile View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''

#====================================================================================================
#UpdateProfile
#====================================================================================================

@api_view(['POST','GET'])
def TranslatorUpdateProfile_API(request):
    if request.method == 'POST':
        username = request.data.get("username") #to acces the data
        # serializer=TranslatorUpdateProfileSerializer(username)
        # return Response(serializer.data)

        # #acces the old data for the user
        try:
            user = User.objects.get(username=username)
        except:
            return Response({"message": "there is no user with this username"})
        try:
           translator = Translatorr.objects.get(user_id=user.id)
        except:
            return Response({"message": "there is no translator with this username"})

        # #the new data from the front-end
        name = request.data.get("name")
        age = request.data.get("age")
        email = request.data.get("email")
        phone = request.data.get("phone")
        # password = make_password(request.data.get("password"))        
        firstLanguage = request.data.get("firstLanguage")
        SecoundLanguage = request.data.get("SecoundLanguage")
        bio = request.data.get("bio")
        price = request.data.get("price")
        gender = request.data.get("gender")
        # # save the data

        user.email=email 
        # user.password= password
        translator.name=name
        translator.age=age
        translator.phoneNumber=phone
        translator.First_Language=firstLanguage
        translator.Second_Language=SecoundLanguage
        translator.Bio=bio
        translator.price=price
        translator.gender=gender
        translator.save()
        user.save()
        return Response({"message": "your informations saved sussesfully"})
    return Response({"message": "hi inter the username"})


@api_view(['POST','GET'])
def CustomerUpdateProfile_API(request):
    if request.method == 'POST':
        username = request.data.get("username") #to acces the data

        # #acces the old data for the user
        try:
            user = User.objects.get(username=username)
        except:
            return Response({"message": "there is no user with this username"})
        try:
           customer = Customer.objects.get(user_id=user.id)
        except:
            return Response({"message": "there is no translator with this username"})

        # #the new data from the front-end
        name = request.data.get("name")
        age = request.data.get("age")
        email = request.data.get("email")
        phone = request.data.get("phone")
        # password = make_password(request.data.get("password"))        
        firstLanguage = request.data.get("firstLanguage")
        gender = request.data.get("gender")
        # # save the data
        print('hiii',request.data )

        user.email=email 
        # user.password= password
        customer.name=name
        customer.age=age
        customer.phoneNumber=phone
        customer.First_Language=firstLanguage
        customer.gender=gender
        customer.save()
        user.save()
        return Response({"message": "your informations saved sussesfully"})
    return Response({"message": "hi inter the username"})


#====================================================================================================
#END UpdateProfile
#====================================================================================================
'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% '''
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
#Star sign Up View
#====================================================================================================
#**Start customer and translator sign up View  the are the same code it for going to deffrent forms **
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status

def CustomerSignUp_View(request):
    form=CustomerSignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request, user)
        return redirect('customer_Home_Page')
    return render(request,'customerSignUp.html', {'form':form})

#customer_signup API
@api_view(['POST'])
def customer_signup(request):
    if request.method == 'POST':
        data = request.data
        print("\n\n\n data: ",data)
        form = CustomerSignUpForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'This endpoint only accepts POST requests.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


def TranslatorSignUp_View(request):
    form=TranslatorSignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request, user)
        return redirect('translator_Home_Page')
    return render(request,'translatorSignUp.html', {'form':form})

#api_view API ----------------------------------------
@api_view(['POST'])
def Translator_signup(request):
    print("\n\n\n before: ",request.data)
    if request.method == 'POST':
        data = request.data
        print("\n\n\n data: ",data)
        form = TranslatorSignUpForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'This endpoint only accepts POST requests.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
#Admin API thi hedin
@api_view(['POST'])
def Admin_signup(request):
    if request.method == 'POST':
        data = request.data
        print("\n\n\n data: ",data)
        form = AdminSignUpForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'This endpoint only accepts POST requests.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#====================================================================================================
#End sign Up View
#====================================================================================================

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

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

#====================================================================================================
#Star Send request View
#====================================================================================================

def witePage_View(request):
    if request.method == 'POST':
        id = request.data.get("translator")
        print('\n\n\n user id: ', id, '\n\n\n')
        translator = Translator.objects.get(user_id=id)
        translatorName= translator.name #get the name of the translator
        translatorID= translator.user_id #get the id of the translator

        current_user  = request.user #to get the user
        current_userId = current_user.id #for storing user id
        customer = Customer.objects.get(user_id=current_userId) #to get the info of translator
        customerName=customer.name
        appointment = Appointment.objects.create(customerName=customerName,translatorName = translatorName, customerID=current_userId, translatorID=translatorID,  accepted=False)
        appointment.save()
        print('\n\n\n\n Id: ', appointment.id , '\n\n\n\n')
        appointment={'appointment': appointment}
        return render(request,'Homes/whitePage.html', appointment)  

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
#Start Machine translation
#====================================================================================================
from googletrans import Translator
def translate_app(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        translator = Translator()
        tr = translator.translate(txt, dest=lang)
        return render(request, 'Pages/translate.html', {"result":tr.text})
    return render(request, 'Pages/translate.html')
#====================================================================================================
#End Machine translation
#====================================================================================================

'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''

#====================================================================================================
#Start Accept/Reject translation
#====================================================================================================
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment  

def accept_appointment(request): 
    requestId = request.POST.get('request_id', None)
    appointment = get_object_or_404(Appointment, pk=requestId) 
    appointment.accepted = 1  
    appointment.save()  
    return render(request, 'Homes/translatorHomePage.html') 

#API-------------------------------------------------
@api_view(['POST','GET'])
def accept_appointment_API(request): 
    if request.method == 'POST':
        id = request.data.get("appointmentID")
        appointment = get_object_or_404(Appointment, pk=id) 
        appointment.accepted = 1  
        appointment.save()  
        serializer=AppointmentSerializer(appointment)
        return Response(serializer.data) 
    return Response({"message": "Enter Appointment ID for accept: appointmentID "})



def reject_appointment(request):  
    requestId = request.POST.get('request_id', None)
    appointment = get_object_or_404(Appointment, pk=requestId) 
    appointment.accepted = 2  
    appointment.save()
    return render(request, 'Homes/translatorHomePage.html')

#API------------------------------------------------------------
@api_view(['POST','GET'])
def reject_appointment_API(request): 
    print('\n\n\n hi:')
    if request.method == 'POST':
        id = request.data.get("appointmentID")
        print('\n\n\n appointmentID:', id)
        appointment = get_object_or_404(Appointment, pk=id) 
        appointment.accepted = 2
        appointment.save()  
        serializer=AppointmentSerializer(appointment)
        return Response(serializer.data) 
    return Response({"message": "Enter Appointment ID for Reject: appointmentID "})

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

def TranslatorHomePage_View(request):
    try:  
        translator=request.user
        translatorID=translator.id
        appointment= Appointment.objects.filter(translatorID=translatorID)
        print('\n\n\n', translatorID, '\n\n\n' )
        x={'appointment': appointment}  
        return render(request,'Homes/translatorHomePage.html',x)#for show the customer Home page 
    except Translator.DoesNotExist :
            return render(request,'Homes/translatorHomePage.html')#for show the customer Home page 
    return render(request,'Homes/translatorHomePage.html')#for show the customer Home page 

#API-----------------------------------------------------------
@api_view(['GET', 'POST'])
def TranslatorHomePage_API(request):
    print('\n\n\n here')
    if request.method == 'POST':  
        translatorUsername = request.data.get("username")
        try:
            print('\n\n\n username:', translatorUsername)
            translator= User.objects.get(username=translatorUsername)
        except:
           return Response({"message":"there is no translator with this username"})#for show the customer Home page          
        translatorID=translator.id
        try:
            appointment= Appointment.objects.filter(translatorID=translatorID, accepted=0)
        except:
           return Response({"message":"there is no translation request yet"})#for show the customer Home page          
        serializer=AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)#for show the customer Home page 
    return Response({"message":"enter translator Username"})#for show the customer Home page 

#====================================================================================================
#End Translator Home page  
#====================================================================================================

'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''

###################################

#====================================================================================================
#Start payment  
#====================================================================================================

import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Product


stripe.api_key = settings.STRIPE_SECRET_KEY

#class SuccessView(TemplateView):
 #   template_name = "success.html"


#class CancelView(TemplateView):
 #   template_name = "cancel.html"

class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.get(name= id.translatorName)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update(
            {"product": products, "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY}
        )
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "https://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": product.price,
                        "product_data": {
                            "name": product.name,
                        },
                    },
                    "quantity": 1,
                },
            ],
            metadata={"product_id": product.id},
            mode="payment",
            success_url=YOUR_DOMAIN + "/success/",
            cancel_url=YOUR_DOMAIN + "/cancel/",
        )
        return JsonResponse({"id": checkout_session.id})

#====================================================================================================
#connect back to front 
#====================================================================================================


#====================================================================================================
#connect DashBoard 
#====================================================================================================
@api_view(['POST','GET'])
def Dashboard(request):  
    if request.method == 'GET':
        users_count = User.objects.all().count()
        appointment_count = Appointment.objects.all().count()
        customers_count = User.objects.filter(is_customer=True).count()
        translators_count = User.objects.filter(is_translator=True).count()
        accepted_appointments_count = Appointment.objects.filter(accepted=1).count()
        accepted_rejected_count = Appointment.objects.filter(accepted=2).count()
        accepted_ongoing_count = Appointment.objects.filter(accepted=0).count()
        print('\n\n\n in')
        return Response({
            "users_count": users_count,
            "appointment_count": appointment_count,
            "customers_count": customers_count,
            "translators_count": translators_count,
            "accepted_appointments_count": accepted_appointments_count,
            "accepted_rejected_count": accepted_rejected_count,
            "accepted_ongoing_count": accepted_ongoing_count
        })











from rest_framework.generics import ListCreateAPIView
from .serializers import Product, CheckoutSessionSerializer

class CheckoutSessionView(ListCreateAPIView):
    serializer_class = CheckoutSessionSerializer
    queryset = Product.objects.all()

'''from django.shortcuts import render
from .models import TranslationRequest

def translation_requests_list(request):
    translation_requests = TranslationRequest.objects.filter(translator=None)

    return render(request, 'translation_requests_list.html', {'translation_requests': translation_requests})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

def my_view(request, translator_id):
    try:
        translator = get_object_or_404(Translator, pk=translator_id)
    except Translator.DoesNotExist:
        return HttpResponseNotFound("Translator not found")
    # do something with the translator object
    return HttpResponse("Translator found: {}".format(translator.name))

from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Translator, TranslationRequest
@csrf_exempt
def accept_request(request, translator_id, request_id):
    try:
        translator = get_object_or_404(Translator, pk=translator_id)
        translation_request = get_object_or_404(TranslationRequest, pk=request_id, translator=translator)
    except (Translator.DoesNotExist, TranslationRequest.DoesNotExist):
        return HttpResponseNotFound("Request not found")
    
    # update the status of the translation request to "accepted"
    translation_request.status = 'accepted'
    translation_request.save()

# return a JSON response with the updated request data
    data = {
        'id': translation_request.id,
        'source_language': translation_request.source_language,
        'target_language': translation_request.target_language,
        'text': translation_request.text,
        'status': translation_request.status,
        'customer': {
            'id': translation_request.customer.id,
            'name': translation_request.customer.name,
            'email': translation_request.customer.email
        }
    }
    return JsonResponse(data)

@csrf_exempt
def reject_request(request, translator_id, request_id):
    try:
        translator = get_object_or_404(Translator, pk=translator_id)
        translation_request = get_object_or_404(TranslationRequest, pk=request_id, translator=translator)
    except (Translator.DoesNotExist, TranslationRequest.DoesNotExist):
        return HttpResponseNotFound("Request not found")
    
    # update the status of the translation request to "rejected"
    translation_request.status = 'rejected'
    translation_request.save()

    # return a JSON response with the updated request data
    data = {
        'id': translation_request.id,
        'First_Language': translation_request.First_Language,
        'Second_Language': translation_request.Second_Language,
        'text': translation_request.text,
        'status': translation_request.status,
        'customer': {
            'id': translation_request.customer.id,
            'name': translation_request.customer.name,
            'email': translation_request.customer.email
        }
    }
    return JsonResponse(data)

'''

from django.http import JsonResponse


from django.http import HttpResponse

def check_status(request):
  appointment = Appointment.objects.get(user=request.user)
  return HttpResponse(str(appointment.accept))  
