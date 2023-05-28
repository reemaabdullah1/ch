from django.urls import path, include
from .views import *


urlpatterns = [   

    #Start home page for login and signup paths =====================================
    path('', home , name='home'),
    #End home page for login and signup paths =======================================

    #Start register page for signup as customer or translators paths ================
    path('register/', index, name='signUp'),
    #Start register page for signup as customer or translators paths ================

    #Start of sign up paths =========================================================
    path('customerSignUp', CustomerSignUp_View, name='customer_signup'),
    path('CustomerSignupAPI/', customer_signup, name='customer_signupAPI'),
    
    path('translatorSignUp', TranslatorSignUp_View, name='translator_signup' ),
    path('translatorSignUpAPI', Translator_signup, name='translator_signupAPI' ),
    
    path('Admin_signup', Admin_signup, name='Admin_signup' ),
    path('Dashboard', Dashboard, name='Dashboard' ),
    
    
    #End of sign up paths ===========================================================
    
    #Start of log in paths ==========================================================
    path('login/', login_view, name='login'),
    path('loginAPi/', login_view2, name='login2'), #API-----------------------------
    path('check_username/', check_username, name='check_username'),
    
    
    #End of log in paths ============================================================

    #Start of Home pages paths ======================================================
    path('customerHomePage', CustomerHomePage_View, name='customer_Home_Page'),
    path('CustomerHomePage_API', CustomerHomePage_API, name='CustomerHomePage_API'),#API--
    
    
    path('translatorHomePage', TranslatorHomePage_View, name='translator_Home_Page' ),
    path('translatorHomePage_API', TranslatorHomePage_API, name='TranslatorHomePage_API' ),
    
    #End of Home pages paths =========================================================

    #Start of send request to the data paths ==========================================
    path('waitingPage', witePage_View, name = 'w'),
    path('create_appointment', create_appointment, name='create_appointment'),#API--
    #End of send request to the data paths ============================================

    #Start machine translation page paths =============================================
    path('translate/', translate_app, name='MachineTranslation'), # Machine translation page
    #End machine translation page paths ===============================================

    #Start CustomerProfile page paths =============================================
    path('CustomerProfile_API', CustomerProfile_API, name='CustomerProfile_API'),
    path('CustomerUpdateProfile_API/', CustomerUpdateProfile_API, name='CustomerUpdateProfile_API'),
    
    path('translatorProfile_API', translatorProfile_API, name='translatorProfile_API'),
    path('TranslatorUpdateProfile_API/', TranslatorUpdateProfile_API, name='TranslatorUpdateProfile_API'),
    #End CustomerProfile page paths =============================================

    #Start CustomerChat page paths =============================================
    path('Chat', CustomerChat_View, name='CustomerChat'),
    path('CustomerRequest_API', CustomerRequest_API, name='CustomerRequest_API'),
    
    #End CustomerChat page paths =============================================
    #Start translatorChat page paths =============================================
    path('TranslatorRequest_API', TranslatorRequest_API, name='TranslatorRequest_API'),
    #End translatorChat page paths =============================================

    #Accept/reject Customer request  paths =============================================
    path('accept_appointment', accept_appointment, name='accept_appointment'),
    path('accept_appointment_API', accept_appointment_API, name='accept_appointment_API'),
    
    path('reject_appointment', reject_appointment, name='reject_appointment'),
    path('reject_appointment_API', reject_appointment_API, name='reject_appointment_API'),
    path('cancel_appointment_API', cancel_appointment_API, name='cancel_appointment_API'),
    path('paid', paid, name='paid'),
    
    #End Accept/reject Customer request  paths
    #Start payment
    path('product-landing-page/', ProductLandingPageView.as_view(), name='ProductLandingPageView'), 
    path("create-checkout-session/<pk>/", CreateCheckoutSessionView.as_view(), name="create-checkout-session",),
    path('checkStatus/', check_status, name='checkStatus'),    
]

