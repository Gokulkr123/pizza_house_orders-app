from django.shortcuts import render, redirect, get_object_or_404
from .forms import PizzaForm
from .models import Pizza
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def create_data(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createfood')
    else:
        form = PizzaForm()
    return render(request, 'create.html', {'form': form})

def read_data(request):
    food_list = Pizza.objects.all()
    return render(request, 'view.html', {'food_list': food_list})

def update_data(request, pk):
    food = Pizza.objects.get(pk=pk)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('viewfood')
    else:
        form = PizzaForm(instance=food)
    return render(request, 'update.html', {'form': form})

def delete_data(request, pk):
    food = Pizza.objects.get(pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('viewfood')
    return render(request, 'delete.html', {'food': food})

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('createfood')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('viewfood')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context = {'user': request.user}
    return render(request, 'logout.html', context)

@login_required
def generate_pdf(request, pk):
    food = get_object_or_404(Pizza, pk=pk)
    template = get_template('pizza_pdf.html')
    html = template.render({'food': food})
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(food.cphonenumber)
        return response
