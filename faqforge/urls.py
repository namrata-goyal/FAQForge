from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faqs/', include('faqs.urls')),  # Include FAQ app URLs
]
