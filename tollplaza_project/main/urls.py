# main/urls.py
from django.urls import path
from .views import register, user_login, dashboard, credit_ewallet, check_balance, user_logout, enter_toll_fee,transaction_history

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('credit-ewallet/', credit_ewallet, name='credit_ewallet'),
    path('check-balance/', check_balance, name='check_balance'),
    path('logout/', user_logout, name='logout'),
    path('enter-toll-fee/', enter_toll_fee, name='enter_toll_fee'),
    path('transaction-history/', transaction_history, name='transaction_history'),

]
