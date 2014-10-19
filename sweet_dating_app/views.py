# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sweet_dating_app.forms import EmailUserCreationForm, PortfolioForm
from sweet_dating_app.models import Portfolio


def home(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')

@login_required
def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        print "form"
        if form.is_valid():
            print "form is valid"
            Portfolio.objects.create(user=request.user,
                                     gender=form.cleaned_data['gender'],
                                     age=form.cleaned_data['age'],
                                     target_gender=form.cleaned_data['target_gender'],
                                     user_photo=form.cleaned_data['user_photo'],
                                    )
            return redirect("profile")
    else:
        form = PortfolioForm()
    data = {"form": form}
    return render(request, 'add_portfolio.html', data)

@login_required
def profile(request):
    if Portfolio.objects.get(user=request.user):
        portfolio_data = Portfolio.objects.get(user=request.user)
        return render(request, 'profile.html', {'portfolio_data': portfolio_data})
    return render(request, 'profile.html', {})


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })