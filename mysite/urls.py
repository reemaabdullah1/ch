
from django.contrib import admin
from django.urls import path, include
from app.views import (CreateCheckoutSessionView,ProductLandingPageView,)

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path("", ProductLandingPageView.as_view(), name="landing-page"),
    path("create-checkout-session/<pk>/",CreateCheckoutSessionView.as_view(), name="create-checkout-session",),
]
