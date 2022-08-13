from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('rus_zam/', views.get_details_rus_zam, name="rus_zam_details"),
    path('rus_zam_tr/', views.display_transaction_rus_zam, name="rus_zam_tr"),
]
