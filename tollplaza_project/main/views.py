# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, CreditForm
from .models import User

# main/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard upon successful registration
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def credit_ewallet(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user = request.user
            user.money_in_ewallet += amount
            user.save()
            return redirect('dashboard')
    else:
        form = CreditForm()
    return render(request, 'credit_ewallet.html', {'form': form})

@login_required
def check_balance(request):
    user = request.user
    return render(request, 'check_balance.html', {'balance': user.money_in_ewallet})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


from .forms import TollFeeForm
from .models import Transaction

@login_required
def enter_toll_fee(request):
    if request.method == 'POST':
        form = TollFeeForm(request.POST)
        if form.is_valid():
            car_number = form.cleaned_data['car_number']
            toll_fee = form.cleaned_data['toll_fee']

            # Check if the user has sufficient balance
            user = request.user
            if user.money_in_ewallet >= toll_fee:
                # Deduct toll fee from user's e-wallet
                user.money_in_ewallet -= toll_fee
                user.save()

                # Record the transaction
                transaction = Transaction.objects.create(
                    user=user,
                    car_number=car_number,
                    toll_fee=toll_fee
                )

                # Display success message or redirect to transaction history
                return render(request, 'main/enter_toll_fee_success.html', {'transaction': transaction})
            else:
                # Display insufficient balance message
                return render(request, 'main/enter_toll_fee_error.html', {'error_message': 'Insufficient balance'})

    else:
        form = TollFeeForm()

    return render(request, 'main/enter_toll_fee.html', {'form': form})

@login_required
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'main/transaction_history.html', {'transactions': transactions})
