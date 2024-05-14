from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('product/',views.product),
    path('additional-features/',views.additionalFeatures),
    path('supported/',views.supported),
    # path('qaac/',views.qaac),
    # path('dal/',views.dal),
    # path('pmsas/',views.pmsas),
    path('why-gofresh/',views.whyGofresh),
]
