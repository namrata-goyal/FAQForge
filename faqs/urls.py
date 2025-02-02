from django.urls import path
from . import views

urlpatterns = [
    path('', views.FAQList.as_view(), name='faq-list'),
]
