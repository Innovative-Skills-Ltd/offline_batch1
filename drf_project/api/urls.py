from django.urls import path
from .views import customerListCreateView, customerDetailView,UserRegisterView

urlpatterns = [
    path('customers/', customerListCreateView.as_view(), name='book-list-create'),
    path('customers/<int:pk>/', customerDetailView.as_view(), name='book-detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
]