from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactCreateView.as_view(), name='contacts_view'),
    path('<int:contact_id>/', views.ContactDetailsView.as_view(), name='contacts_view'),
]